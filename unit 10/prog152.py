import sys
sys.setrecursionlimit(5000)

def multi():
    a=0
    for i in range(3,9670,3):
        a+=i
    return a

print(multi())

# 15586428

def bmulti():
    a=0
    for i in range(9669,0,-3):
        a+=i
    return a

print(bmulti())

# 15586428

def recurv(n):
    if n==3:
        return 3
    return n+recurv(n-3)

print(recurv(9669))

# 15586428