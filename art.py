import time

try:
	import requests
except ImportError as exc:
	print("Error: failed to import settings module ({})".format(exc))

try:
    import database.mysql as db
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))

try:
    import wikipedia as wiki
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))


class art():

	def __init__(self, artid, verbose = 0):
		self.id = str(artid)
		self.conn = db.connect()
		self.cursor = self.conn.cursor()
		self.verbose = verbose
		self.info = 0

	def fetch_info(self):
		sql = "SELECT ID, OBJECTNUMBER, PRINCIPALMAKER, TITLE, year_ FROM artwork WHERE ID = "+self.id
		if self.verbose:
			print sql
		result = db.read(sql, self.cursor)
		if self.verbose:
			print result
		self.objet_number = result[0][1]
		self.artist = result[0][2]
		self.title = result[0][3]
		self.year = result[0][4]
		self.info = 1

	def describe_title(self):
		if self.info == 0:
			self.fetch_info()
		(wiki_title_results, wiki_title_suggestions) = wiki.search(self.title, suggestion = True)
		if len(wiki_title_results) > 0:
			a = wiki_title_results[0]
		elif wiki_title_suggestions!=None:
			a = wiki_title_suggestions[0]
		else:
			return 0
		# print type(a)
		print self.title
		summary = wiki.summary(a)
		summary_word_list = summary.split()
		summary_size = len(summary_word_list)
		if (summary_size > 30):
			print summary
			print "\n"
		else:
			print "incorrect summary:"
			print summary
			print "\n" 
		# if wiki.summary(a)