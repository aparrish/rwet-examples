import sys
import random

def get_words_from_file(filename):
  all_words = list()
  for line in open(filename):
    line = line.strip()
    words = line.split(" ")
    for word in words:
      all_words.append(word)
  return all_words

words_from_file = get_words_from_file("sowpods.txt")

for line in sys.stdin:
  line = line.strip()
  words = line.split(" ")
  output = ""
  for word in words:
    if random.randrange(8) == 0:
      output += random.choice(words_from_file)
    else:
      output += word
    output += " "
  print output
