evens = [n for n in range(0,11) if n%2==0]
odds = [n+1 for n in evens[:-1]]

# .count(enter variable or number/string) will count any of that requested variable

# sets - subset. make a set then check a subset with var.issubset(nums)

# if looking to round up, need to do the following: x=int(round((n+5)//10)*10)