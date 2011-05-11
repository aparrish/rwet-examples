stuff = {
	'cat': {
		'name': 'Monsieur Whiskeurs',
		'fur': 'tortoise',
		'toy': {
			'name': 'plush catnip ravioli',
			'price': 'six dollars'
		}
	},
	'dog': {
		'name': 'Scrambles',
		'fur': 'golden',
		'outfit': {
			'scarf': 'tartan',
			'pants': {
				'color': 'green',
				'style': 'chinos'
			}
		}
	}
}

def print_dictionary_values(x):
	# if x is a dictionary, iterate through each value and call this function
	# on those values
	if type(x) == dict:
		for key in x.keys():
			print_dictionary_values(x[key])
	# otherwise, just print the value out
	else:
		print x

print_dictionary_values(stuff)

