import sys

words = set()

for line in sys.stdin:
	line = line.strip()
 	line_words = line.split()
 	for word in line_words:
		words.add(word)

for word in words:
	print word
