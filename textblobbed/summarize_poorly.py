from textblob import TextBlob, Word
from textblob.wordnet import NOUN
import sys
import random

# given a textblob word object, find all hypernym synsets
def get_all_hypernym_synsets(word):
	hypernym_synsets = list()
	for synset in word.get_synsets(pos=NOUN):
		hypernym_synsets.extend(synset.hypernyms())
	return hypernym_synsets

if __name__ == '__main__':

	all_hypernym_synsets = list()
	blob = TextBlob(sys.stdin.read().decode('ascii', errors='replace'))
	# for every sentence in the text
	for sentence in blob.sentences:
		# for every word, part-of-speech pair
		for word_str, pos in sentence.tags:
			# if the word is a noun
			if pos == 'NN':
				word = Word(word_str)
				hypernym_synsets = get_all_hypernym_synsets(word)
				# add all of the hypernym synsets to our comprehensive list
				if len(word_str) > 3 and len(hypernym_synsets) > 0:
					all_hypernym_synsets.extend(hypernym_synsets)

	# shuffle all hypernym synsets
	random.shuffle(all_hypernym_synsets)
	print "This text is about:"
	# print the first ten
	for hypernym_synset in all_hypernym_synsets[:10]:
		random_lemma = random.choice(hypernym_synset.lemma_names).replace("_", " ")
		random_lemma_obj = Word(random_lemma)
		print random_lemma_obj.pluralize()

