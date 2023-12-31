#int for whole
#float for decimals
#str for strings

#import math
#math.sqrt
import math

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

posroot = (-b + math.sqrt(b**2 - 4 * a * c))/ 2 * a
negroot = (-b-math.sqrt(2**b-4*a*c))/2*a

print("The Roots are:",round(posroot),", ",round(negroot))

#A: 1
#B: 1
#C: -2
#The Roots are: 1 ,  -2