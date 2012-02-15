import sys
import random

source_alpha = dict()
source_file = sys.argv[1] # first argument passed on command line

# read each line from source file; split each line into words; store each
# word in the source_alpha dictionary, according to which letter it starts with
for line in open(source_file):
  line = line.strip()
  words = line.split(" ")
  for word in words:
    if len(word) > 0: # check to make sure we have a word
      first_letter = word[0]
      # if we've already seen this letter, append to list
      if first_letter in source_alpha: 
        source_alpha[first_letter].append(word)
      else:
        source_alpha[first_letter] = [word]

# source_alpha will be a dictionary whose keys are strings and whose values
# are lists.
# uncomment this to see what the data structure created above looks like
#print source_alpha

# read each line from standard input; split line into words; for each word,
# get a random word beginning with the same letter from source_alpha
for line in sys.stdin:
  line = line.strip()
  words = line.split(" ")
  output = list()
  for word in words:
    if len(word) > 0:
      first_letter = word[0]
      if first_letter in source_alpha:
        source_words = source_alpha[first_letter]
        output.append(random.choice(source_words))
      else:
        output.append(word)
  print " ".join(output)

