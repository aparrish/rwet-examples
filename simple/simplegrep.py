import sys

searchstr = "you"

for line in sys.stdin:
	line = line.strip()
	if searchstr in line:
		print line
