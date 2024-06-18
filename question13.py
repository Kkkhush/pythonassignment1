# QUESTION 13. Write a program that asks the user for their birth year and calculates their age.

def age(current_year, birth_year):
    age = current_year - birth_year
    print(age)

current_year = int(input("Enter current year: "))
birth_year = int(input("Enter your year of birth: "))
x = age(current_year, birth_year)
print(x)