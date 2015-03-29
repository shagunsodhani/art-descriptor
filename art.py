import time

try:
    import database.mysql as db
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))

try:
    import wikipedia as wiki
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))


class art():

	def __init__(self, artist, title, verbose = 0, stopwords = {}):
		# self.id = artid
		self.artist = artist
		self.title = title
		self.verbose = verbose
		self.info = 0
		self.stopwords = stopwords

	def describe_title(self):
		(wiki_title_results, wiki_title_suggestions) = wiki.search(self.title, suggestion = True)
		if len(wiki_title_results) > 0:
			a = wiki_title_results[0]
		elif wiki_title_suggestions!=None:
			a = wiki_title_suggestions[0]
		else:
			return 0
		# print type(a)
		# print self.title
		summary = wiki.summary(a)
		summary_word_list = summary.split()
		summary_size = len(summary_word_list)
		print "summary : "
		print summary
		print "title : "
		print self.title
		flag = 0
		if (summary_size > 30):
			# print summary
			# print "summary size > 30"
			title_word_list = self.title.split()
			for i in title_word_list:
				if i not in self.stopwords:
					if i not in summary_word_list:
						flag = -1
						print i
						# break;

		# else:
			#summary too small
			#try generating summary using artist name



	def describe_artist(self):
		if self.verbose:
			print "Generating information for artist ", self.artist
		wiki_artist_results = wiki.search(self.artist)
		if len(wiki_artist_results) > 0:
			wiki_id = wiki_artist_results[0]
		else:
			return 0
		page = wiki.page(wiki_id)
		print "Summary about the artist : ", page.summary
		print "content about the artist : ", page.content
		#since artist is a named entity, we do not have to perform tests for resolving artist entity.
