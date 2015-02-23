import unittest
import contextfree

class TestContextFree(unittest.TestCase):
	def test_contextfree(self):
		grammar = {'A': ['B C'], 'C': ['D E']}
		expected = ['B', 'D', 'E']
		self.assertEqual(contextfree.generate_list(grammar, 'A'), expected)

if __name__ == '__main__':
	unittest.main()
