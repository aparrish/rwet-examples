
def ucfirst(s):
  return s[0].upper() + s[1:]

def halfsies(left, right):
  left_part = left[:len(left)/2]
  right_part = right[len(right)/2:]
  return left_part + right_part

def restaurant(building="House", foodstuff="Pancakes"):
  return "International " + building + " of " + foodstuff

def human_join(parts, conjunction):
  if len(parts) == 1:
    return parts[0]
  first_join = ', '.join(parts[:-1])
  return first_join + " " + conjunction + " " + parts[-1]
