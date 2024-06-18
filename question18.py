# QUESTION 18. Write a python program that checks if two strings are anagrams of each other.

def isAnagram(a,b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False

a = input('Enter string a: ')
b = input('Enter string b: ')
x = isAnagram(a,b)
print(x)