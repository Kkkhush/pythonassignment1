# QUESTION 16. Write a program in python that counts the frequency of each character in a string.

string1 = input("Enter any string : ")
dict = {}
for key in string1:
    if key in dict:
        dict[key]+=1
    else:
        dict[key]=1

print("The frequency of each character in the string is: ")

for key, value in dict.items():
    print(key, ":", value)
