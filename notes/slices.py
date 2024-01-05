# Slices use the same syntax as range; goes from start (inclusive) up to a stop index (exclusive)
# list[start:stop] or list[start:stop:step]
# list[:stop] (starts at 0 and goes up to stop) or list[start:] (starts at 'start' and goes to the end of the list)

list1 = [1, 2, 3, 4, 5]
list2 = list1[0:3]  # or [:3]
print(list2)
list3 = list1[3:len(list1)]  # or [3:]
print(list3)
print(list2 + list3)

strHi = "Hello, world!"
substr = strHi[0:5]
print(substr)
print(strHi[-1])
print(strHi[-6:-1])
print(strHi[::-1])  # returns the string in reverse order; also reversed(strHi) works
print(strHi == strHi[::-1])

"""
evens = [n for n in range(0,11) if n%2==0]
odds = [n+1 for n in evens[:-1]


Should print 
0,2,4,6,8,10
1,3,5,7,9
"""

"""
return sum(nums)
"""

"""
product
import math

def wtf(nums):
  return math.prod(nums)
"""

"""
to return a list with all the same numbers, can do return[a]*x (x being the amound of numbers in the list)
"""