
import sys
import random
from restaurantutils import ucfirst, restaurant, human_join

words = list()
for line in sys.stdin:
  line = line.strip()
  words.append(ucfirst(line))

for i in range(10):
  number_to_sample = random.randrange(1, 5)
  things = random.sample(words, number_to_sample)
  print restaurant(random.choice(words), human_join(things, "and"))
