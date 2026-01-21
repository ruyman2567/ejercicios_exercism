"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
  return 'un'+ word


def make_word_groups(vocab_words):
  lista1 = list(vocab_words)
  separator = ' :: '+lista1[0]
  return separator.join(lista1)


def remove_suffix_ness(word):
  if word.endswith('iness'):
    withoutness = word.split('iness')
    original = withoutness[0]
    return(str(original+'y'))
  else:
    withoutness = word.split('ness')
    original = withoutness[0]
    return original


def adjective_to_verb(sentence, index):
  if sentence.endswith('.'):
    oracion=sentence.split('.')
    sentence1 = oracion[0]
    div = sentence1.split(' ')
    word = div[index]
  return word+'en'