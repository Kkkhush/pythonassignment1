# QUESTION 8: Write a python program that concatenates two strings and returns the result.

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

#concatenating two strings and also adding space between them

str3 = str1 +" "+ str2
print(str3)

#sometimes we need to do explixcit typecasting for concatenation of two strings

str3 = "Hello"
str4 = 10

string = str3 + str(10)
print(string)