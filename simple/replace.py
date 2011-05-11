import sys

for line in sys.stdin:
	line = line.strip()
	line = line.replace('woods', 'cheese wheels')
	line = line.replace('Woods', 'Cheese Wheels')
	line = line.replace('snow', 'cheese')
	line = line.replace('Snow', 'Cheese')
	line = line.replace('dark', 'sharp')
	line = line.replace('sleep', 'eat')
	print line
