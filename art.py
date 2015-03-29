import time

try:
	import requests
except ImportError as exc:
	print("Error: failed to import settings module ({})".format(exc))

try:
    import database.mysql as db
except ImportError as exc:
    print("Error: failed to import settings module ({})".format(exc))


class art():

	def __init__(self, artid, artistid):
		self.id = str(artid)
		self.artistid = str(artistid)
		self.conn = db.connect()
		self.cursor = self.conn.cursor()