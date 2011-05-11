import random

conjunctions = ['and', 'or', 'so', 'but', 'yet', 'until', 'before', 'after']

# join together the list in 'parts' with the given conjunction, human-style
# (e.g., "one, two and three" instead of "one, two, three"
def human_join(parts, conjunction="and", oxford=False):
	if len(parts) == 1:
		return parts[0]
	first_part = ', '.join(parts[:-1])
	second_part = parts[-1]
	if oxford:
		conj = ", " + conjunction + " "
	else:
		conj = " " + conjunction + " "
	return conj.join([first_part, second_part])

# join the two parts together using one of the conjunctions defined in this
# module
def random_conjoin(part1, part2):
  return part1 + " " + random.choice(conjunctions) + " " + part2

if __name__ == '__main__':
	import sys
	print human_join(sys.argv[1:], oxford=True)

