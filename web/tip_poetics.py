import urllib
import sys
import time
import json
import random
import re

# to get your own client id/client secret, go here:
#   https://foursquare.com/oauth/
foursq_client_id = sys.argv[1]
foursq_client_secret = sys.argv[2]
latlong = sys.argv[3] # e.g. 40.68,-73.94

# n is the number of search terms to squeeze off the end of the line
n = 3

for line in sys.stdin:

	line = line.strip()

	# if the line is blank, don't bother looking it up
	if len(line) == 0:
		print ""
		continue

	# split line into tokens
	line_tokens = line.split(' ')

	# search foursquare tips for the last n tokens
	query = ' '.join(line_tokens[-n:])

	# we're going to match against this token later to complete the line
	last_token = re.sub(r'\W+$', '', line_tokens[-1])

	# these are the parameters to the search call. they go on the url.
	params = {
		'll': latlong,
		'query': query,
		'client_id': foursq_client_id,
		'client_secret': foursq_client_secret}

	# make the request. urllib.urlencode changes a dictionary into a string
	# in the format key1=val1&key2=val2 (also translating special chars as
	# needed)
	response = urllib.urlopen('https://api.foursquare.com/v2/tips/search?' + \
		urllib.urlencode(params))

	# if the response returned 200 (HTTP for 'it worked!')...
	if response.getcode() == 200:
		# call the response's read() method, which returns the response from
		# the remote server as a string.  pass that to json.loads() ('loads'
		# stands for '_load_ from _s_tring') to decode the data
		data = json.loads(response.read())

		# things we might append to the current line
		possibles = list()

		# now work with the data. we know the data has the format expected here
		# because we (a) checked the documentation, (b) tried the request out with
		# curl first, or, preferably, (c) both!
		for tip in data['response']['tips']:
			tip_tokens = tip['text'].split(' ')
			# find every tip that has the last word in the line from the source
			# text. take everything from that word to the end of the line.
			if last_token in tip_tokens:
				idx = tip_tokens.index(last_token)
				possibles.append(tip_tokens[idx:])

		if len(possibles) > 0:
			from_source = ' '.join(line_tokens[:-1])
			from_foursquare = ' '.join(random.choice(possibles))
			print from_source + " " + from_foursquare
		else:
			print ' '.join(line_tokens)

	else:
		print "error connecting to foursquare! " + str(response.getcode())

	# this tells python not to try to buffer the output, so we see each line
	# as it arrives
	sys.stdout.flush()

	time.sleep(0.5) # wait a while before next request, just to be nice
