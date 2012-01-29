import sys
for line in sys.stdin:
	line = line.strip()
	line = line.replace("the ", "that dadgum ")
	line = line.replace("and ", "and, tell you what, ")
	line = line.replace(" a ", " a doggone ")
	line = line.replace(".", ". Boy, howdy.")
	line = line.replace("!", ", hoooo-weeee!")
	print line
