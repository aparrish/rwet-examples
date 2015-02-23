import random

def build_model(tokens, n):
	"Builds a Markov model from the list of tokens, using n-grams of length n."
	model = dict()
	if len(tokens) < n:
		return model
	for i in range(len(tokens) - n):
		gram = tuple(tokens[i:i+n])
		next_token = tokens[i+n]
		if gram in model:
			model[gram].append(next_token)
		else:
			model[gram] = [next_token]
	final_gram = tuple(tokens[len(tokens)-n:])
	if final_gram in model:
		model[final_gram].append(None)
	else:
		model[final_gram] = [None]
	return model

def generate(model, n, seed=None, max_iterations=100):
	"""Generates a list of tokens from information in model, using n as the
		length of n-grams in the model. Starts the generation with the n-gram
		given as seed. If more than max_iteration iterations are reached, the
		process is stopped. (This is to prevent infinite loops)""" 
	if seed is None:
		seed = random.choice(model.keys())
	output = list(seed)
	current = tuple(seed)
	for i in range(max_iterations):
		if current in model:
			possible_next_tokens = model[current]
			next_token = random.choice(possible_next_tokens)
			if next_token is None: break
			output.append(next_token)
			current = tuple(output[-n:])
		else:
			break
	return output

def merge_models(models):
	"Merges two or more Markov models."
	merged_model = dict()
	for model in models:
		for key, val in model.iteritems():
			if key in merged_model:
				merged_model[key].extend(val)
			else:
				merged_model[key] = val
	return merged_model

def generate_from_token_lists(token_lines, n, count=14, max_iterations=100):
	"""Generates text from a list of lists of tokens. This function is intended
		for input text where each line forms a distinct unit (e.g., poetry), and
		where the desired output is to recreate lines in that form. It does this
		by keeping track of the n-gram that comes at the beginning of each line,
		and then only generating lines that begin with one of these "beginnings."
		It also builds a separate Markov model for each line, and then merges
		those models together, to ensure that lines end with n-grams statistically
		likely to end lines in the original text.""" 
	beginnings = list()
	models = list()
	for token_line in token_lines:
		beginning = token_line[:n]
		beginnings.append(beginning)
		line_model = build_model(token_line, n)
		models.append(line_model)
	combined_model = merge_models(models)
	generated_list = list()
	for i in range(count):
		generated_str = generate(combined_model, n, random.choice(beginnings),
				max_iterations)	
		generated_list.append(generated_str)
	return generated_list

def char_level_generate(lines, n, count=14, max_iterations=100):
	"""Generates Markov chain text from the given lines, using character-level
		n-grams of length n. Returns a list of count items."""
	token_lines = [list(line) for line in lines]
	generated = generate_from_token_lists(token_lines, n, count, max_iterations)
	return [''.join(item) for item in generated]

def word_level_generate(lines, n, count=14, max_iterations=100):
	"""Generates Markov chain text from the given lines, using word-level
		n-grams of length n. Returns a list of count items."""
	token_lines = [line.split() for line in lines]
	generated = generate_from_token_lists(token_lines, n, count, max_iterations)
	return [' '.join(item) for item in generated]

if __name__ == '__main__':
	import sys
	n = int(sys.argv[1])
	lines = list()
	for line in sys.stdin:
		line = line.strip()
		lines.append(line)
	for generated in char_level_generate(lines, n):
		print generated

