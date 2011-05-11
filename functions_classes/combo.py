from WorstPossibleHaikuGenerator import WorstPossibleHaikuGenerator
from Concordance import Concordance
import sys
import random

concord = Concordance()
for line in sys.stdin:
	line = line.strip()
	concord.feed(line)

haikugen = WorstPossibleHaikuGenerator(5, 7, 5)
unique_words = concord.unique_words()
for i in range(100):
	haikugen.add_word(random.choice(unique_words))

most_common = concord.most_common_words(100)
for word in most_common:
	haikugen.add_word(word)

print haikugen.generate()

