from __future__ import unicode_literals
import sys
import random
import spacy

nlp = spacy.load('en')
text = sys.stdin.read().decode('utf8', errors="replace")
doc = nlp(text)

short_sentences = []
for sentence in doc.sents:
    if len(sentence) > 3 and len(sentence) <= 7:
        short_sentences.append(sentence.text)

for sentence in random.sample(short_sentences, 5):
    print sentence
