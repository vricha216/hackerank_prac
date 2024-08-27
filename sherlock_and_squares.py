
import math

def is_sqrt(a):
    num = a**0.5
    if num.is_integer():
        return int(num)
    return False
    

def squares(a, b):
   
    first_sqr = 0
    last_sqr = 0
    
    i = a
    #to find smallest perfect square >= a
    while i<=b:
        if is_sqrt(i):
            first_sqr = is_sqrt(i)
            break;
        i+=1
        
    k = b
    #to find smallest perfect square <=b
    while k>=a:
        if is_sqrt(k):
            last_sqr = is_sqrt(k)
            break;
        k-=1
        
    if not first_sqr and not last_sqr:
        return 0

    return last_sqr - first_sqr +1

a = 24
b = 49
print(squares(a, b))