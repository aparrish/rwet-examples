from __future__ import unicode_literals
import sys
import random
import spacy

nlp = spacy.load('en')
text = sys.stdin.read().decode('utf8', errors="replace")
doc = nlp(text)

people = [item.text for item in doc.ents if item.label_ == 'PERSON']
gerunds = [item.text for item in doc if item.tag_ == 'VBG']

print "What they're doing:"
print ""
for i in range(10):
    print random.choice(people) + " is " + random.choice(gerunds)
print ""
print "Bless their hearts, each and every one."
