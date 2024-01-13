a=int(input("Input number to find the factorial: "))

def recur(n): 
    if n==1: #base case
        return 1
    return n*recur(n-1) #recursive case

a = recur(a)
print(a)

# Input number to find the factorial: 5
# 120

"""
Factorial Calulation

Forward through the factorial
def fact(n):
    summ = 1
    for i in range(1, n+1):
        summ*=i
    return summ

Reverse through the factorial
def factRev(n):
    summ = 1
    for i in range(n, 0,-1):
        summ*=i
    return summ
"""