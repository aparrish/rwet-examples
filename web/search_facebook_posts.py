import json
import urllib
import time

def search_facebook_posts(query):
	resp = urllib.urlopen('http://graph.facebook.com/search?' + urllib.urlencode(query))
	data = json.loads(resp.read())
	posts = list()
	for item in data['data']:
		if 'message' in item:
			posts.append(item)
	return posts

if __name__ == '__main__':

	import sys	
	query = {'q': sys.argv[1], 'limit': 100}

	for post in search_facebook_posts(query):
		print post['message'].encode('ascii', 'replace')

