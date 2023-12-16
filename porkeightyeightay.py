#int for whole
#float for decimals
#str for strings

#import math
#math.sqrt
import math

#absoulute value: abs

a = int(input("A: "))
b = int(input("B: "))

print("Sum: ",sum([a,b]))
print("Diff: ", a-b)
print("Prod: ", a*b)
print("Avg: ",(a+b)/2)
print("Abs: ", abs(a-b))

if a>=b:
    print("Max: ",a)
    print("Min: ",b)
else:
    print("Max: ",b)
    print("Min: ",a)

# A: 13
# B: 20
# Sum:  33
# Diff:  -7
# Prod:  260
# Avg:  16.5
# Abs:  7
# Max:  20
# Min:  13