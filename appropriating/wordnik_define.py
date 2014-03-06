import sys
import urllib
import random
import json

api_key = sys.argv[1]
word = sys.argv[2]

params = {
		'limit': 10,
		'includeRelated': 'false',
		'api_key': api_key
}
url = "http://api.wordnik.com/v4/word.json/" + urllib.quote_plus(word) + \
		"/definitions?" + urllib.urlencode(params)
#print url

urlobj = urllib.urlopen(url)
result = json.loads(urlobj.read())
#print result

if len(result) > 0:
	for definition in result:
		#print definition
		print definition['text']

