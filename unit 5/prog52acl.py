from cl52a import rectangle

a = int(input("A: "))
b = int(input("B: "))

shape = rectangle(a,b)
shape.calc()

print(shape.getarea(), shape.getperem())

"""
A: 143
B: 82
11726 450
"""