import conjunctions

class Sentence(object):

  # initialize function provides default arguments for subject and verb
  def __init__(self, subj="No one", verb="ignored", direct_obj="", 
      prep_phrase=""):
    self.subj = subj
    self.verb = verb
    self.direct_obj = direct_obj
    self.prep_phrase = prep_phrase

  # render puts all the parts of the sentence together, only adding
  # direct object and prepositional phrase if present
  def render(self):
    elems = [self.subj, self.verb]
    if len(self.direct_obj) > 0:
      elems.append(self.direct_obj)
    if len(self.prep_phrase) > 0:
      elems.append(self.prep_phrase)
    output = ' '.join(elems)
    return output

  # statement: renders this sentence as a statement
  def statement(self):
    output = self.render()
    output += "."
    return output

  def question(self):
    return "Is it the case that " + self.render() + "?"

  # uses the conjunctions module to randomly conjoin this sentence with
  # another
  def statement_conjoined_with(self, other_sentence):
    output = conjunctions.random_conjoin(self.render(), other_sentence.render())
    output += "."
    return output

if __name__ == '__main__':
  sentence1 = Sentence('John', 'ate', 'cheese', 'in a sack')
  print sentence1.statement()
  sentence2 = Sentence('George', 'slept')
  print sentence2.statement()
  print sentence1.statement_conjoined_with(sentence2)

