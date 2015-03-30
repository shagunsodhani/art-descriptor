stopword_data = "data/stopword.txt"

def remove_stopwords():	
	stopwords = {}
	with open(stopword_data) as infile:
		for line in infile:
			a = line.strip()
			if a not in stopwords:
				stopwords[a] = 1
	return stopwords