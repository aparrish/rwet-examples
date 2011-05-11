import sys

# will be a list of lists
pairs = list()

for line in sys.stdin:

  # strip line, break into words
  line = line.strip()
  words = line.split(" ")

  # skip this line if there are fewer than two words on it
  if len(words) < 2:
    continue

  # iterate from 0 up to the length of the list minus one (so we don't
  # inadvertently grab elements from beyond the length of the list)
  for i in range(len(words) - 1):
    pair = words[i:i+2] # i.e., the element at i and the next element
    pairs.append(pair)

# print out pairs
for pair in pairs:
  print ' '.join(pair)

