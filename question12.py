# QUESTION 12. Write a python program that calculates the sum of digits of a given number.

def sum(n):

 sum = 0
 for digit in str(n):
        sum = sum +int(digit)

 return sum
n=input("Enter any number of your choice: ")
x = sum(n)
print(x)
