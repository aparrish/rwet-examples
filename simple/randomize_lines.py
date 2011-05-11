import sys
import random

all_lines = list()

for line in sys.stdin:
	line = line.strip()
	all_lines.append(line)

random.shuffle(all_lines)

for line in all_lines:
	print line
