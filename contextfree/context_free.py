
class ContextFree(object):

  def __init__(self):
    self.rules = dict()
    self.expansion = list()

  # rules are stored in self.rules, a dictionary; the rules themselves are
  # lists of expansions (which themselves are lists)
  def add_rule(self, rule, expansion): 
    if rule in self.rules:
      self.rules[rule].append(expansion)
    else:
      self.rules[rule] = [expansion]

  def expand(self, start):

    import random

    # if the starting rule was in our set of rules, then we can expand it 
    if start in self.rules:
      possible_expansions = self.rules[start]
      # grab one possible expansion
      random_expansion = random.choice(possible_expansions)
      # call this method again with the current element of the expansion
      for elem in random_expansion:
        self.expand(elem)
    else:
      # if the rule wasn't found, then it's a terminal: simply append the
      # string to the expansion
      self.expansion.append(start)

  # utility method to run the expand method and return the results
  def get_expansion(self, axiom):
    self.expand(axiom)
    return self.expansion

if __name__ == '__main__':

  cfree = ContextFree()
  cfree.add_rule('S', ['NP', 'VP'])
  cfree.add_rule('NP', ['the', 'N'])
  cfree.add_rule('N', ['cat'])
  cfree.add_rule('N', ['dog'])
  cfree.add_rule('N', ['weinermobile'])
  cfree.add_rule('N', ['duchess'])
  cfree.add_rule('VP', ['V', 'the', 'N'])
  cfree.add_rule('V', ['sees'])
  cfree.add_rule('V', ['chases'])
  cfree.add_rule('V', ['lusts after'])
  cfree.add_rule('V', ['blames'])

  #print cfree.rules

  expansion = cfree.get_expansion('S')
  print ' '.join(expansion)

