import random
comp = random.randint(1,20)

player = int(input("Enter a number between 1 and 20: "))
print("Computer's Number:",comp)
if comp == player:
    print("You Won!")
else:
    print("Better luck next time.")