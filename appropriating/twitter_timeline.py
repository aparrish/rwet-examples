import sys
import twython

api_key, api_secret, access_token, token_secret = sys.argv[1:]

twitter = twython.Twython(api_key, api_secret, access_token, token_secret)
response = twitter.get_user_timeline(screen_name='aparrish', count=50)

for tweet in response:
	print tweet['text']

