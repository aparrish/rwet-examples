import sys
import random

for line in sys.stdin:
	line = line.strip()
	words = line.split(" ")
	random.shuffle(words)
	output = " ".join(words)
	print output
