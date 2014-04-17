from textblob import TextBlob
import sys
import random

text = sys.stdin.read().decode('ascii', errors="replace")
blob = TextBlob(text)

noun_phrases = blob.noun_phrases

verbs = list()
for word, tag in blob.tags:
	if tag == 'VB':
		verbs.append(word.lemmatize())

for i in range(1, 11):
	print "Step " + str(i) + ". " + random.choice(verbs).title() + " " + \
			random.choice(noun_phrases)

