
import sys
import random

def ucfirst(s):
  return s[0].upper() + s[1:]

def restaurant(building="House", foodstuff="Pancakes"):
  return "International " + building + " of " + foodstuff

def human_join(parts, conjunction):
  if len(parts) == 1:
    return parts[0]
  first_join = ', '.join(parts[:-1])
  return first_join + " " + conjunction + " " + parts[-1]

words = list()
for line in sys.stdin:
  line = line.strip()
  words.append(ucfirst(line))

for i in range(10):
  number_to_sample = random.randrange(1, 5)
  things = random.sample(words, number_to_sample)
  print restaurant(random.choice(words), human_join(things, "and"))
