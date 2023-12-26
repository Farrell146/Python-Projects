from cl54c import circle

a = float(input("A: "))

shape = circle(a)
shape.calc()

print(shape.getarea(),shape.getcir())