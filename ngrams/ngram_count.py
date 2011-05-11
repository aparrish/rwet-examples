
# NGramCounter builds a dictionary relating ngrams (as tuples) to the number
# of times that ngram occurs in a text (as integers)
class NGramCounter(object):

  # parameter n is the 'order' (length) of the desired n-gram
  def __init__(self, n):
    self.n = n
    self.ngrams = dict()

  # feed method calls tokenize to break the given string up into units
  def tokenize(self, text):
    return text.split(" ")

  # feed method takes text, tokenizes it, and visits every group of n tokens
  # in turn, adding the group to self.ngrams or incrementing count in same
  def feed(self, text):

    tokens = self.tokenize(text)

    # e.g., for a list of length 10, and n of 4, 10 - 4 + 1 = 7;
    # tokens[7:11] will give last three elements of list
    for i in range(len(tokens) - self.n + 1):
      gram = tuple(tokens[i:i+self.n])
      if gram in self.ngrams:
        self.ngrams[gram] += 1
      else:
        self.ngrams[gram] = 1

  def get_ngrams(self):
    return self.ngrams

if __name__ == '__main__':

  import sys

  # create an NGramCounter object and feed data to it
  ngram_counter = NGramCounter(5)
  for line in sys.stdin:
    line = line.strip()
    ngram_counter.feed(line)

  # get ngrams from ngram counter; iterate over keys, printing out keys with
  # a count greater than one
  ngrams = ngram_counter.get_ngrams()
  for ngram in ngrams.keys():
    count = ngrams[ngram]
    if count > 1:
      print ' '.join(ngram) + ": " + str(count)

