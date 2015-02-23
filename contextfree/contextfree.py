import random

def generate_list(grammar, axiom):
	"""Generate a list of tokens from grammar, starting with axiom. The grammar
		should take the form of a dictionary, mapping rules (strings) to lists
		of expansions for those rules. Expansions will be split on whitespace.
		Any token in the expansion that doesn't name a rule in the grammar will
		be included in the expansion as-is."""
	s = list()
	if axiom in grammar:
		expansion = random.choice(grammar[axiom])
		for token in expansion.split():
			s.extend(generate_list(grammar, token))
	else:
		s.append(axiom)
	return s

if __name__ == '__main__':
	import sys
	import json
	grammar = json.loads(sys.stdin.read())
	axiom = sys.argv[1]
	sentence = ' '.join(generate_list(grammar, axiom))
	sentence = sentence[0].upper() + sentence[1:] + "."
	print sentence

