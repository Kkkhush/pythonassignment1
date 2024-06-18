# QUESTION 14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.


l=[]
while(True):
    line = input("Enter the line: ")
    if(line==''):
        break
    else:
        l.append(line)
for i in l:
    print(i)