# Lists are already like arraylists
# Instead, here are dictionaries and tuples

# Dictionaries store key-value pairs || Key on the left : Value on the right
dctnry = {}
dctnry2 = {1: "apples", 2: "oranges", 3: "pears"}
dctnry3 = {"name": "John", "clr": "red", 0: [1, 2, 3]}

print(dctnry2[2])
print(dctnry3["name"])
print(dctnry2)
print(dctnry2.keys()) #returns the keys of a dict
print(dctnry2.values()) #returns the values of a dict


# Tuples store groups of variables
tpl = (1, 2, 3)
# They can be unpacked -- super useful for returning multiple vals from one function
x, y, z = tpl

print(tpl == (x, y, z))  # Repack x,y,z

def returnMulti():
    return 3, 5, 7

a, b, c = returnMulti()
print(a, b, c)
print(returnMulti())