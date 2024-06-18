# QUESTION 1: Write a program which takes two numbers as input and print their sum.

# method 1 : without using function
num1 = int(input("Enter the value of first number: "))
num2 = int(input("Enter the value of second number: "))

num3 = num1 + num2
print("The sum of the two numbers is: ", num3)


# method 2 : using function
def sum(num1, num2):
    sum = num1 + num2
    print("The value of sum of two numbers is: ", sum)
    return

# call function
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum(num1, num2)

