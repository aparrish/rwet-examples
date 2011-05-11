import sys

words = dict()

for line in sys.stdin:
	line = line.strip()
	line_words = line.split(" ")
	for word in line_words:
		if word in words:
			words[word] += 1
		else:
			words[word] = 1

for word in words.keys():
	print word + ": " + str(words[word])
