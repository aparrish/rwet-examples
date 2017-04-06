from __future__ import unicode_literals
import sys
import random
import spacy

nlp = spacy.load('en')
text = sys.stdin.read().decode('utf8', errors="replace")
doc = nlp(text)

noun_phrase_text = [item.text.strip() for item in doc.noun_chunks]
verbs = [item.lemma_ for item in doc if item.pos_ == 'VERB']

for i in range(1, 11):
    instruction = random.choice(verbs).title() + " " + random.choice(noun_phrase_text)
    print "Step " + str(i) + ". " + instruction

