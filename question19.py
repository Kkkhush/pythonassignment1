# QUESTION 19. Write a python program that removes all punctuations from a string.

string = input("Enter any string value: ")
print("The original string is: ", string)
str1 = ""
for i in string:
    if i not in['.','','!','@','?',':',';','"','_','&','$','*','^','{}','[]','()','~']:
        str1 = str1 +i
print("The string after removing all the punctuations from the string: ", str1)