import random
import numpy as np

# Make an Array. Fill it with 19 random numbers from 20 to 90
nums = [random.randint(20,90) for lcv in range(19)]

# Print the Array from the beginning to the end
print(nums) # could use, enumerate - for lcv,n in enumerate(nums)

# Print the Array from the beginning to the end using a for-each loop
for num in nums:
    print(num,end=" ") #gives you the object within the list instead of the full list due to it being a for each loop
    
print()

# What number is in the middle of the Array?
print(nums[len(nums)//2]) #double divide is floor divide which rounds down to the nearest int

# What is the average of the first, last and middle numbers?
print((nums[0]+nums[len(nums)//2]+nums[-1])/3)

# Find the smallest and the largest number in the Array
print(min(nums),max(nums))

# Switch the largest with smallest number. Print the list
sind = np.argmin(nums)
mind = np.argmax(nums)

temp = min(nums)

nums[sind] = max(nums)
nums[mind] = temp
print(nums)

# Create a new random from 1 to 10 and insert it in the middle slot. Print the numbers.
nums[len(nums)//2]=random.randint(1,10)
print(nums)

# Add 10 to every number in the List. Print all.
for lcv in range(len(nums)):
    nums[lcv]+=10
print(nums)

# Replace the 3rd element in the array with 5 and print the number that was ousted (only use one method to complete this.)
old=nums[4]
nums[4]=5
print(old)

# What numbers are in the 50s?
print([n for n in nums if 49 < n < 60]) #example of list comprehension, building a set with words

# What numbers are multiples of 4?
print([n for n in nums if n%4==0])

# Is there a 60 in the list?
if 60 in nums:
    print("Yes")

# Check to see if all of the elements from front to back are in the same order from back to front
print(nums[::-1]==nums)

# How many numbers are greater than the average?
avgnums=np.average(nums)
checker=0
for lcv in range(len(nums)):
    if nums[lcv]>avgnums:
        checker+=1
print(checker)

# How many of the numbers are even?
evens = len([n for n in nums if n%2==0])
print(evens)

# Copy all of the elements of the array into a new array but in reverse order
opposite = nums[::-1]
print(opposite)

# Write a program to shift every element of an array circularly right. E.g.-INPUT : 1 2 3 4 5 OUTPUT : 5 1 2 3 4
# def circularshiftright(array):
#     return array[:1]+array[1:]
# shiftedright=circularshiftright(nums)
print(np.roll(nums,1))

# Find the sum of all of the digits of all of the elements
sum=0
for num in nums:
    digitsum=0
    temp=num
    while temp>0:
        b = temp%10
        temp/=10
        digitsum+=num
    sum+=digitsum
print("Sum:",sum)
