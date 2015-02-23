import unittest
import cmudict

class TestCMUDict(unittest.TestCase):
	def test_parse_cmu(self):
		cmufh = open("cmudict-0.7b")
		pronunciations = cmudict.parse_cmu(cmufh)
		self.assertGreater(len(pronunciations), 0)
		matches = [x for x in pronunciations if x[0] == 'adolescent']
		self.assertEqual(len(matches), 2)
	def test_syllable_count(self):
		self.assertEqual(cmudict.syllable_count("CH IY1 Z"), 1)
		self.assertEqual(cmudict.syllable_count("CH EH1 D ER0"), 2)
		self.assertEqual(cmudict.syllable_count("AE1 F T ER0 W ER0 D"), 3)
		self.assertEqual(cmudict.syllable_count("IH2 N T ER0 M IH1 T AH0 N T"), 4)
		self.assertEqual(
				cmudict.syllable_count("IH2 N T ER0 M IH1 T AH0 N T L IY0"), 5)
	def test_phones_for_word(self):
		phones = cmudict.phones_for_word("conflicts")
		self.assertEqual(len(phones), 4)
		self.assertEqual(phones[0], "K AH0 N F L IH1 K T S")
	def test_rhyming_part(self):
		part = cmudict.rhyming_part("S L IY1 P ER0")
		self.assertEqual(part, "IY1 P ER0")
		part = cmudict.rhyming_part("S L IY1 P AH0 L IY0")
		self.assertEqual(part, "IY1 P AH0 L IY0")
	def test_search(self):
		matches = cmudict.search('^S K L')
		self.assertEqual(matches,
				['sclafani', 'scleroderma', 'sclerosis', 'sklar', 'sklenar'])
	def test_rhymes(self):
		cmufh = open("cmudict-0.7b")
		pronunciations = cmudict.parse_cmu(cmufh)
		rhymes = cmudict.rhymes("sleekly")
		expected = ['beakley', 'biweekly', 'bleakley', 'meekly', 'obliquely',
				'steakley', 'szekely', 'uniquely', 'weakley', 'weakly', 'weekley',
				'weekly', 'yeakley']
		self.assertEqual(expected, rhymes)

if __name__ == '__main__':
	unittest.main()
