import unittest
import ngramcount

class TestNgramCount(unittest.TestCase):
	def test_count_ngrams(self):
		tokens = list("condescendences")
		expected = {
				('d', 'e'): 2,
				('n', 'd'): 2,
				('n', 'c'): 1,
				('s', 'c'): 1,
				('e', 's'): 2,
				('e', 'n'): 2,
				('o', 'n'): 1,
				('c', 'o'): 1,
				('c', 'e'): 2}
		self.assertEqual(ngramcount.count_ngrams(tokens, 2), expected)
	def test_merge_counts(self):
		model_a = {('a', 'b'): 1, ('d', 'e'): 1}
		model_b = {('a', 'b'): 1, ('e', 'f'): 1}
		expected = {('a', 'b'): 2, ('d', 'e'): 1, ('e', 'f'): 1}
		self.assertEqual(ngramcount.merge_counts([model_a, model_b]), expected)

if __name__ == '__main__':
	unittest.main()
