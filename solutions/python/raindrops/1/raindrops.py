def convert(number):
    palabras = ''
    if number%3 == 0:
        palabras+= 'Pling'
    if number%5 == 0:
        palabras+= 'Plang'
    if number%7==0:
        palabras+= 'Plong'
    if not palabras:
        return str(number)
    else:
        return palabras