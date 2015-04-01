
def ucfirst(s):
  return s[0].upper() + s[1:]

if __name__ == '__main__':
  import sys
  for line in sys.stdin:
    line = line.strip()
    if len(line) > 0:
      print ucfirst(line)
    else:
      print line
