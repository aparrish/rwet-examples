import context_free
import re

def add_rules_from_file(cfree, file_obj):
  # rules are stored in the given file in the following format:
  # Rule -> a | a b c | b c d
  # ... which will be translated to:
  # self.add_rule('Rule', ['a'])
  # self.add_rule('Rule', ['a', 'b', 'c'])
  # self.add_rule('Rule', ['b', 'c', 'd'])
  for line in file_obj:
    line = re.sub(r"#.*$", "", line) # get rid of comments
    line = line.strip() # strip any remaining white space
    match_obj = re.search(r"(\w+) *-> *(.*)", line)
    if match_obj:
      rule = match_obj.group(1)
      expansions = re.split(r"\s*\|\s*", match_obj.group(2))
      for expansion in expansions:
        expansion_list = expansion.split(" ")
        cfree.add_rule(rule, expansion_list)

if __name__ == '__main__':

  cfree = context_free.ContextFree()
  add_rules_from_file(cfree, open("test.grammar"))
  expansion = cfree.get_expansion('S')
  print ' '.join(expansion)

