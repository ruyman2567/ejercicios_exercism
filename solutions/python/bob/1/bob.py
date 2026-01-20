def response(hey_bob):
  lista1= list(hey_bob)
  if hey_bob.isupper() and not('?' in hey_bob) :
    return 'Whoa, chill out!'
  elif len(lista1)==0 or hey_bob.isspace():
    return 'Fine. Be that way!'
  elif hey_bob.endswith('?') and hey_bob.isupper():
    return "Calm down, I know what I'm doing!"
  elif hey_bob.strip().endswith('?'):
    return 'Sure.'
  else:
    return 'Whatever.'