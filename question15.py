# QUESTION 15.Write a program that reads data from csv file and prints it to the console.

import csv
f= open("C:\pythonassignment\pythoncsv.csv",'r')

freader= csv.reader(f)
for row in freader:
    print(row)
print("Data printed successfully")
f.close()
