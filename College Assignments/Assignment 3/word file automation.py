question_list = ["Accept enrollno, name and marks of 5 subjects of 5 students from user and write in a CSV file.","Accept emp no, name and salary from user and write only those rows in CSV file where salary is more than 5000.","Write a Python list to a CSV file. After writing the CSV file, read the CSV file and display the contents.","Write a CSV file to read any given CSV file as a dictionary.","Count the total number of records present in a CSV file and print it.","Write a Python program to read first 3 rows (excluding the header) of a CSV file.","Consider the below mentioned CSV file invoice.csv. Read the contents of this file in python and display the total billing amount in Python."]

for i in range(1, 8):
    print(f"Problem Statement - {i}",end="\n")
    print(question_list[i-1],end="\n\n")
    print("Source Code:",end="\n\n\n")
    print("CSV File:",end="\n\n\n\n")
    print("Sample Input and Output:",end="\n\n\n\n")