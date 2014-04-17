from textblob import TextBlob
import sys

pos = sys.argv[1]

for line in sys.stdin:
	line = line.strip()
	blob = TextBlob(line)
	for word, tag in blob.tags:
		if tag == pos:
			print word

