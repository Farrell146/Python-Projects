try: 
    a = 0
    b = 0
    with open ("data/prog215a.dat") as f:
        lines = f.readlines()
        for line in lines:
            c = int(line)
            if c<500:
                a+=1
            else:
                b+=1

    print("Less than 500:",a)
    print("Is or Greater than 500:",b)
    print("Total numbers:",a+b)

except Exception as e:
    print(e)

"""
Less than 500: 192
Is or Greater than 500: 208
Total numbers: 400
"""

"""
with open ("data/prog215a.dat") as f: - opens up a data file
        lines = f.readlines() - lines is declared as a list
        for line in lines:  - will automatically add 1 to the line variable
"""