from textblob import Word
import sys
import random

for line in sys.stdin:
	line = line.strip()
	line = line.decode('ascii', errors="replace")
	words = line.split(" ")
	output = list()
	for word_str in words:
		word_obj = Word(word_str)
		if len(word_str) > 3 and len(word_obj.synsets) > 0:
			random_synset = random.choice(word_obj.synsets)
			random_lemma = random.choice(random_synset.lemma_names)
			output.append(random_lemma.replace('_', ' '))
		else:
			output.append(word_str)
	print " ".join(output)

