# QUESTION 11. Write a python program that generates the first n numbers in the fibonacci series.

n = int(input("Enter the number of terms you want to generate of fibonacci series: "))
a = 0
b = 1
c = a+b
print("The first", n, "numbers of fibpnacci series are: ")
for i in range(n):
    print(a,end =" ")
    a = b
    b = c
    c = a+b







