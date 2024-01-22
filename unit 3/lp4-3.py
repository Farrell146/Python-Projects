eggs = int(input("Number of eggs: "))

# "//" divides then rounds down to nearest int (floor divide)
doz = eggs//12

# "%" is modulus - the remainder of long division
rem = eggs%12

calc = 0

if 0 < doz <= 4:
    calc = .50
elif doz > 4 and doz <= 6:
    calc = .45
elif doz > 6 and doz <= 11:
    calc = .40
elif doz > 11:
    calc = .35

print("The bill is equal to: $"+str((doz*calc)+(rem*(calc*(1/12)))))

"""Number of eggs: 18
The bill is equal to: $0.75"""