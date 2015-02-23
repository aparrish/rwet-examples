import unittest
import markov

class TestMarkov(unittest.TestCase):
	def test_build_model(self):
		tokens = list("condescendences")
		expected = {
				('d', 'e'): ['s', 'n'],
				('n', 'd'): ['e', 'e'],
				('n', 'c'): ['e'],
				('s', 'c'): ['e'],
				('e', 's'): ['c', None],
				('e', 'n'): ['d', 'c'],
				('o', 'n'): ['d'],
				('c', 'o'): ['n'],
				('c', 'e'): ['n', 's']}
		self.assertEqual(markov.build_model(tokens, 2), expected)
	def test_generate(self):
		model = {
				('a', 'b'): ['c'],
				('b', 'c'): ['d'],
				('c', 'd'): [None]}
		self.assertEqual(['a', 'b', 'c', 'd'],
				markov.generate(model, 2, ('a', 'b')))
	def test_max_iterations(self):
		model = {
				('a', 'b'): ['c'],
				('b', 'c'): ['d'],
				('c', 'd'): ['c'],
				('d', 'c'): ['d']}
		expected = list('abcdcdc')
		self.assertEqual(markov.generate(model, 2, ('a', 'b'), max_iterations=5),
				expected)
	def test_merge_models(self):
		model_a = {('a', 'b'): ['c'], ('d', 'e'): ['f']}
		model_b = {('a', 'b'): ['d'], ('e', 'f'): ['g']}
		expected = {('a', 'b'): ['c', 'd'], ('d', 'e'): ['f'], ('e', 'f'): ['g']}
		self.assertEqual(markov.merge_models([model_a, model_b]), expected)

if __name__ == '__main__':
	unittest.main()
