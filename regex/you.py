import sys
import re

for line in sys.stdin:
  line = line.strip()
  if re.search(r'\b[Yy]ou\b', line):
    print line

