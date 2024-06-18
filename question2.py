# QUESTION 2: Write a program to check whether a given number is even or odd.

num = int(input("Enter any number of your choice: "))
# use of conditional statements
# if statement is used to check if remainder is zero or not
if num % 2 == 0:
    print("The given number", num, "is an even number")
    # if remainder is zero on dividing by 2 , then the number is even.

else:
    print("The given number", num, "is an odd number")

