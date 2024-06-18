# QUESTION 3: Write a python program that calculate the factorial of a given number.

def function_fact(num):
    if (num == 1) or (num == 0):
        return 1
    elif num<0:
        print("Cannot calculate factorial of negative numbers")
    else:
        return(num * function_fact(num-1))


num = int(input("Enter any number: "))
print(f"The factorial of number {num}  is: ", function_fact(num))
