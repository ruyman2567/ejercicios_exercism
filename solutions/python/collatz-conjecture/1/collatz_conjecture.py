def steps(number):
    act=0
    contador=0
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    else:
        while number!=1:
          contador+=1
          if number%2==0:
            div2 = number/2
            number = div2
            #print(number)
          else:
            mult= number*3 +1
            number = mult
            #print(number)
    return contador 
            