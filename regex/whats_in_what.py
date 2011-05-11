import sys
import re

data = dict()

for line in sys.stdin:
  line = line.strip()
  for match_obj in re.finditer(r"\b(\w+) in the (\w+)", line):
    contained = match_obj.group(1)
    container = match_obj.group(2)
    contained = contained.lower()
    container = container.lower()
    if container in data:
      data[container].append(contained)
    else:
      data[container] = list()
      data[container].append(contained)

for container in data.keys():
  contained_list = data[container]
  all_contained = ', '.join(contained_list)
  print container + ": " + all_contained

