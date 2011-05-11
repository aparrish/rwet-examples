import sys

def load_adjectives():
  adj = set()
  for line in open('adjectives'):
    line = line.strip()
    adj.add(line)
  return adj

adj_set = load_adjectives()

for line in sys.stdin:
  line = line.strip()
  adjs = [s for s in line.split(" ") if s.lower() in adj_set]
  if len(adjs) > 0:
    print ', '.join(adjs)

