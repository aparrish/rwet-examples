import markov

class CharacterMarkovGenerator(markov.MarkovGenerator):
	def tokenize(self, text):
		return list(text)
	def concatenate(self, source):
		return ''.join(source)

if __name__ == '__main__':

	import sys

	generator = CharacterMarkovGenerator(n=8, max=500)
	lines = set()
	for line in sys.stdin:
		line = line.strip()
		generator.feed(line)

	for i in range(14):
		print generator.generate()

