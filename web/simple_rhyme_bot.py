import sys
import urllib
import json
import time
import random

def get_examples(api_key, word):
	resp = urllib.urlopen(
			'http://api.wordnik.com/v4/word.json/' + word + '/examples?' + \
			urllib.urlencode({'api_key': api_key}))
	examples_data = json.loads(resp.read())
	examples = [item['text'] for item in examples_data['examples']]
	return examples

def get_random_word(api_key):
	resp = urllib.urlopen(
			'http://api.wordnik.com/v4/words.json/randomWord?' +
			urllib.urlencode({'minCorpusCount': 10000, 'api_key': api_key}))
	random_word_data = json.loads(resp.read())
	return random_word_data['word']

def get_rhyming(api_key, word):
	resp = urllib.urlopen(
			'http://api.wordnik.com/v4/word.json/' + word + '/relatedWords?' + \
			urllib.urlencode({'api_key': api_key, 'relationshipTypes': 'rhyme'}))
	related_data = json.loads(resp.read())
	if len(related_data) == 0:
		return []
	else:
		return related_data[0]['words']

def up_to_and_including_word(line, word):
	word_ends = line.find(word) + len(word)
	return line[:word_ends]

if __name__ == '__main__':
	wordnik_key = sys.argv[1]

	while True:

		# sleep so as to not inadvertently appear to be a DDoS attack
		time.sleep(0.5)

		# get a random word, attempt to get random words
		current_word = get_random_word(wordnik_key)
		rhyming_words = get_rhyming(wordnik_key, current_word)
		if len(rhyming_words) == 0:
			# if no words rhymed with the random word, try another
			continue

		# get a random example sentence for this word
		examples = get_examples(wordnik_key, current_word)
		example = random.choice(examples)
		print up_to_and_including_word(example, current_word)

		# get a random example sentence for one of the rhyming words
		rhyme = random.choice(rhyming_words)
		rhyme_examples = get_examples(wordnik_key, rhyme)
		rhyme_example = random.choice(rhyme_examples)
		print up_to_and_including_word(rhyme_example, rhyme)

