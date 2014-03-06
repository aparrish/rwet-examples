import sys
import urllib
import random
import json
import time

api_key = sys.argv[1]

for line in sys.stdin:
	line = line.strip()
	words = line.split()
	output = list()
	for word in words:
		if len(word) < 5:
			output.append(word)
		else:
			params = {
				'useCanonical': 'false',
				'relationshipTypes': 'rhyme',
				'limitPerRelationshipType': 100,
				'api_key': api_key
			}
			url = "http://api.wordnik.com/v4/word.json/" + \
					urllib.quote_plus(word) + \
					"/relatedWords?" + \
					urllib.urlencode(params)
			#print url
			urlobj = urllib.urlopen(url)
			result = json.loads(urlobj.read())
			#print result
			if len(result) > 0 and len(result[0]['words']) > 0:
				rhymes = result[0]['words']
				output.append(random.choice(rhymes))
			else:
				output.append(word)
	print " ".join(output)
	time.sleep(0.5)

