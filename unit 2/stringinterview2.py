# short answer: if sorted(a.lower()) == (b.lower())

amt = int(input("Amount of Words to Check: "))
words=[]
birds=[]
for lcv in range(amt):
    bird=input("Word "+str(lcv+1)+": ")
    words.append(bird)
    birds.append(sorted((bird.lower()).replace(' ','')))

for checker in range(len(birds)):
    base=birds[checker]
    for hecker in range(checker,len(birds)):
        yup=birds[hecker]
        if base==yup and (words[checker] != words[hecker]):
            print(str(words[checker])+" is the Anagram of "+str(words[hecker]))

"""
Amount of Words to Check: 5
Word 1: boss hoss
Word 2: mary
Word 3: army
Word 4: rescue 
Word 5: secure
mary is the Anagram of army
rescue is the Anagram of secure
"""

"""
proper way to check two strings:
if (len(str) == len(str2) and (all(char in str2 for char in str1) and all(char instr1 for char in str2))

# Also see any()
"""