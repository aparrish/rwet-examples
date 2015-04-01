
import sys

def ucfirst(s):
  return s[0].upper() + s[1:]

for line in sys.stdin:
  line = line.strip()
  if len(line) > 0:
    print ucfirst(line)
  else:
    print line
