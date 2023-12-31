colors = ["red", "green", "blue"]
print(colors)
print(colors[1])

fruits = ["apple", "banana", "orange", "kiwi", "mango"]
print(len(fruits))
for index in range(len(fruits)):
  print(fruits[index])

print()
for fruit in fruits:
  print(fruit)  # For-each loop

# lastfruit = fruits[len(fruits) - 1]
lastfruit = fruits[-1]
print(lastfruit)

"""
def reverse3(nums):
  # rev = [nums[2], nums[1], nums[0]]
  rev = []
  rev.append(nums[2])
  rev.append(nums[1])
  rev.append(nums[0])
  return rev

def middle_way(a, b):
  midA = a[1]
  midBIndex = len(b)//2  # int(round(len(b)/2))
  midB = b[midBIndex]
  return [midA, midB]
"""