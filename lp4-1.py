copies = int(input("Numbers of Copies: "))
ppc = 0

if copies <= 99 and copies > 0:
    ppc = .30
elif copies > 99 and copies <= 499:
    ppc = .28
elif copies > 499 and copies <= 749:
    ppc = .27
elif copies > 749 and copies <= 1000:
    ppc = .26
elif copies > 1000:
    ppc = .25

print("Price per copy: $"+str(ppc))
print("Total cost: $"+str(ppc*copies))

# comma automatically puts in a space inbetween the

"""Numbers of Copies: 1001
Price per copy: $0.25
Total cost: $250.25"""