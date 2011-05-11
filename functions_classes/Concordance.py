
class Concordance(object):

	def __init__(self):
		self.concord = dict()

	def tokenize(self, line):
		return line.split(" ")

	def feed(self, line):
		words = self.tokenize(line)
		for word in words:
			if word not in self.concord:
				self.concord[word] = 0
			self.concord[word] += 1

	def count_for_word(self, word):
		if word in self.concord:
			return self.concord[word]
		else:
			return 0

	def unique_words(self):
		return self.concord.keys()

	def reverse_sorted_pairs(self):
		# magic words for getting a list of word/count pairs, sorted in reverse
		# order by count
		return list(sorted(self.concord.iteritems(), key=lambda x: x[1],
			reverse=True))

	def most_common_words(self, num):
		pairs = self.reverse_sorted_pairs()
		# return a list with just the first item (the word) from the reverse sorted
		# list of word/count pairs (up to num items)
		return [p[0] for p in pairs[:num]]

	def get_concordance(self):
		return self.concord

if __name__ == '__main__':

	import sys
	concordance = Concordance()
	for line in sys.stdin:
		line = line.strip()
		concordance.feed(line)

	unique_word_count = len(concordance.unique_words())
	print "number of unique words in input: " + str(unique_word_count)

	the_count = concordance.count_for_word('the')
	print "the word 'the' appears " + str(the_count) + " times"

	print "top twenty words, in order of frequency:"
	pairs = concordance.reverse_sorted_pairs()
	for pair in pairs[:20]:
		print "\t" + pair[0] + ": " + str(pair[1])

