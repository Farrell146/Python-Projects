a="aeoiu"
b="aaabcdiii"
c=sorted(a+b)
print(c)
e=0
letter=""

list=[]

for i in range(len(c)):
    if letter != c[i]:
        if e<c.count(c[i]) or e==c.count(c[i]):
            e=c.count(c[i])
            letter=c[i]
            list.append(letter)

print(list)