def count_ngrams(tokens, n):
	"""Returns a dictionary mapping tuples of n-grams with order n to the number
		of times that n-gram occurred in list tokens."""
	ngrams = dict()
	if len(tokens) < n:
		return ngrams
	for i in range(len(tokens) - n + 1):
		ngram = tuple(tokens[i:i+n])
		if ngram not in ngrams:
			ngrams[ngram] = 0
		ngrams[ngram] += 1
	return ngrams

def merge_counts(ngrams_list):
	"""Returns a dictionary with counts merged from a list of n-gram count
		dictionaries (such as that returned from count_ngrams)."""
	merged = dict()
	for ngrams in ngrams_list:
		for key, val in ngrams.iteritems():
			if key not in merged:
				merged[key] = 0
			merged[key] += val
	return merged

if __name__ == '__main__':
	import sys
	n = int(sys.argv[1])
	counts = list()
	for line in sys.stdin:
		line = line.strip()
		counts.append(count_ngrams(list(line), n))
	combined_counts = merge_counts(counts)
	sorted_counts = sorted(combined_counts.items(), key=lambda x: x[1],
			reverse=True)
	for key, val in sorted_counts:
		print ''.join(key) + ": " + str(val)

