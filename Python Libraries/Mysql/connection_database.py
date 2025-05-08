import mysql.connector as connector

con = connector.connect(host="localhost", port="3306", user="root", password="", database="python_tests")
print(con)