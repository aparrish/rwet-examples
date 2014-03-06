import sys
import time
import twython

api_key, api_secret, access_token, token_secret = sys.argv[1:]

twitter = twython.Twython(api_key, api_secret, access_token, token_secret)

for line in sys.stdin:
	line = line.strip()
	if len(line) > 0:
		response = twitter.search(q=line, result_type='recent', count=1)
		if len(response['statuses']) > 0: 
			first_tweet = response['statuses'][0]
			print first_tweet['text']
		else:
			print line
		time.sleep(0.5)

