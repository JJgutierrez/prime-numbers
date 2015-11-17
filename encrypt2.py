#Using the Python language, have the function PrimeMover(num) 
#return the numth prime number. The range will be from 1 to 10^4. For example: 
#if num is 16 the output should be 53 as 53 is the 16th prime number.
from math import sqrt

def PrimeMover(num,nth):
    nth = input('Enter a number : ') 
    nth = int(nth)
    nth2 = (nth - 1)
    prime = [2]
    
    for c in range(3,num):
        e = round(sqrt(c)) + 1
        for d in prime:
            if d <= e and c%d==0:
                break
                
        else:
            prime.extend([c])
    print (prime[nth2])
    
    
      
PrimeMover(10000,"")    
    