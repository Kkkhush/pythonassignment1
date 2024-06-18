# QUESTION 25. Write a program that copies the contents of one text file to another.

f = open("C:\pythonassignment\pythonmlassignment.txt",'r')
data = f.read()
f.close()
f1 = open("C:\pythonassignment\pythonassignment2.txt",'w')
f1.writelines(data)
print("The data has been written successfully into this file.")
f1.close()


