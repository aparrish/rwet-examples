import json
import urllib
import time

def search_twitter(query):
	resp = urllib.urlopen('http://search.twitter.com/search.json?' + urllib.urlencode(query))
	data = json.loads(resp.read())
	tweets = list()
	for item in data['results']:
		tweets.append(item)
	return tweets

if __name__ == '__main__':

	import sys	
	query = {'q': sys.argv[1], 'rpp': 100}

	for tweet in search_twitter(query):
		print tweet['text'].encode('ascii', 'replace')

