import sys
import random

# A simple example of how to parse and search the CMU pronouncing dictionary.
# Feed the CMU pronouncing dictionary file to this script as standard input.

sss_words = list()

for line in sys.stdin:
	line = line.strip()
	if line.startswith(';'): continue
	word, phones = line.split("  ")
	syllable_count = phones.count('0') + phones.count('1') + phones.count('2')
	if phones.startswith('S ') and syllable_count == 1:
		sss_words.append(word.lower())

print ' '.join(random.sample(sss_words, 5))

