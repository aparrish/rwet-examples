import random

class WorstPossibleHaikuGenerator(object):

	def __init__(self, firstline, secondline, thirdline):
		self.linelengths = [firstline, secondline, thirdline]
		self.words = list()

	def add_word(self, word):
		self.words.append(word)

	def generate(self):
		lines = list()
		for length in self.linelengths:
			this_line = ' '.join([random.choice(self.words) for x in range(length)])
			lines.append(this_line)
		return '\n'.join(lines)

if __name__ == '__main__':
	import sys
	haikugen = WorstPossibleHaikuGenerator(5, 7, 5)
	for line in sys.stdin:
		line = line.strip()
		words = line.split(" ")
		for word in words:
			haikugen.add_word(word)

	print haikugen.generate()

