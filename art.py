import time
import re
import nltk

try:
    import wikipedia as wiki
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))

try:
    from summary import SimpleSummarizer
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))


class art():

	def __init__(self, title, artist, object_number, verbose = 0, stopwords = {}, artist_summary_size = 4, title_summary_size = 4):
		self.artist = artist
		self.title = title
		self.object_number = object_number
		self.verbose = verbose
		self.info = 0
		self.stopwords = stopwords
		self.artist_summary_size = artist_summary_size
		self.title_summary_size = title_summary_size

	def describe_title(self):
		(wiki_title_results, wiki_title_suggestions) = wiki.search(self.title, suggestion = True)
		if len(wiki_title_results) > 0:
			wiki_id = wiki_title_results[0]
		elif wiki_title_suggestions!=None:
			wiki_id = wiki_title_suggestions[0]
		else:
			return 0
		page = wiki.page(wiki_id)
		ss = SimpleSummarizer()
		porter_stemmer = nltk.stem.porter.PorterStemmer()
		wordnet_lemmatizer = nltk.stem.WordNetLemmatizer()	
		summary = page.summary
		summary_word_list_temp = summary.split()
		summary_word_list = []
		for i in summary_word_list_temp:
			token = wordnet_lemmatizer.lemmatize(porter_stemmer.stem(i.lower()))
			summary_word_list.append(token)

		summary_size = len(summary_word_list)
		print "summary : "
		print summary
		print "title : "
		print self.title
		if (summary_size > 30):
			title_word_list = self.title.split()
			# print title_word_list
			for i in title_word_list:
				a = i.encode('ascii','ignore')
				token = wordnet_lemmatizer.lemmatize(porter_stemmer.stem(a.strip().lower()))
				token = token.encode('ascii','ignore')
				count = 0				
				if token not in self.stopwords:
					if token not in summary_word_list and token not in summary_word_list_temp:
						count+=1
			if count < 0.4*len(title_word_list):
				#summary accepted
				print "summary accepted"			
				content = ""
				a = re.split('\n==[A-Za-z ]*==\n', page.content.split('== References ==')[0])
				for i in a:
					content+=i.strip()+"\n"
				if self.verbose:
					print "Wikipedia Summary about the art-piece : ", page.summary
					print "\n"
					print "Generated Summary about the art-peice : ", ss.summarize(content, self.title_summary_size)
					print "\n"
					print "Content about the art-peice : ", content
					print "\n"
		else:
			print "Scrape karenge!"
						


	def describe_artist(self):

		if self.verbose:
			print "Generating information for artist ", self.artist
		wiki_artist_results = wiki.search(self.artist)
		if len(wiki_artist_results) > 0:
			wiki_id = wiki_artist_results[0]
		else:
			return 0
		page = wiki.page(wiki_id)
		ss = SimpleSummarizer()
		content = ""
		a = re.split('\n==[A-Za-z ]*==\n', page.content.split('== References ==')[0])
		for i in a:
			content+=i.strip()+"\n"
		if self.verbose:
			print "Wikipedia Summary about the artist : ", page.summary
			print "\n"
			print "Generated Summary about the artist : ", ss.summarize(content, self.artist_summary_size)
			print "\n"
			print "Content about the artist : ", content
			print "\n"
		for i in page.links:
			print i

		print self.title
		# print page.links