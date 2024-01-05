checker = input("Enter word: ")
a=len(checker)
for base in range(len(checker)):
    for yup in range(base+1,len(checker)):
        if checker[base] == checker[yup]:
            a-=1

print("Unique Letters:",a)

"""
Enter word: java
Unique Letters: 3
"""