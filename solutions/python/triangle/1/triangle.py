def equilateral(sides):
    a,b,c =sides 
    if a==b==c== 0:
      return False
    elif a==b==c:
            if a + b >= c:
                if b+c>= a:
                    if a + c>=b:
                        return True         
    else:
        return False

def isosceles(sides):
    a,b,c = sides
    if a==b or  c==a or b==c:
        if a + b >= c:
                if b+c>= a:
                    if a + c>=b:
                        return True
                    else:
                        return False
                else: 
                    return False
        else: 
            return False  
    else:
        return False


def scalene(sides):
    a,b,c = sides
    if a!=b and b!=c and a!=c:
        if a + b >= c:
                if b+c>= a:
                    if a + c>=b:
                        return True
                    else:
                        return False
                else: 
                    return False
        else: 
            return False  
    else:
        return False
