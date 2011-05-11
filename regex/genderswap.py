import re
import sys

for line in sys.stdin:
  line = line.strip()
  line = re.sub(r'\b[Hh]im\b', 'her', line)
  line = re.sub(r'\b[Hh]e\b', 'she', line)
  line = re.sub(r'\b[Hh]is\b', 'her', line)
  print line

