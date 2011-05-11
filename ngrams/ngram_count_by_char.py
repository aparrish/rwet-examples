import ngram_count

class CharacterNGramCounter(ngram_count.NGramCounter):
  def tokenize(self, text):
    return list(text)

if __name__ == '__main__':

  import sys

  # create an NGramCounter object and feed data to it
  ngram_counter = CharacterNGramCounter(5)
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

