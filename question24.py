# QUESTION 24. Write a program that acts as a simple calculator. It should take two numbers and operator(+, -, *, /)
# as input and print the result

# calculator
# defining basic functions

def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2

# giving list of choice to user

print("Choose required operation \n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n")
choice = int(input("Enter the required operation from choices given: "))
# taking input -> num1 and num2

num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))

if choice == 1:
    print(num1, "+", num2, "=", addition(num1, num2))

elif choice == 2:
    print(num1, "-", num2, "=", subtraction(num1, num2))

elif choice == 3:
    print(num1, "*", num2,"=", multiplication(num1, num2))

elif choice == 4:
    print(num1, "/", num2, "=",division(num1, num2))

else:
    print("INVALID OUTPUT")




