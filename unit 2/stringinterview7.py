def is_vowel(str1):
    vowel = "aeiou"
    
    return any(char in str1 for char in vowel) # can skip writing out vowel and use "any(char in str1 for char in "aeiou")"

word = input("Enter: ")
a=0

for checker in range(len(word)):
    if is_vowel(word[checker]):
        a+=1


print(str(a),"vowels and",str(len(word)-a)," consonants")

"""
Enter: java
2 vowels and 2  consonants
"""