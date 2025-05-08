# Can only run in terminal

import getpass

username = input("Enter the username:")
password = getpass.getpass("Enter your password:")
confirm = getpass.getpass("Confirm your password:")

if password == confirm:
    print("Login successful!")
else:
    print("Wrong Password!")