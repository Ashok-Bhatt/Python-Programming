from dbhelper import DBHelper

db1 = DBHelper()

while True:

    print("\n\n1. Fetch All     2. Fetch from id    3. Insert data    4. Update data    5. delete data")
    choice = int(input("Enter choice: "))

    if choice == 1:
        db1.fetch_all()
    elif choice == 2:
        id = int(input("Enter the id of user: "))
        db1.fetch_user_info(id)
    elif choice == 3:
        id = int(input("Enter the id of user: "))
        name = input("Enter the name of user: ")
        phone = input("Enter the phone number of user: ")
        db1.insert(id, name, phone)
    elif choice == 4:
        id = int(input("Enter the id of user: "))
        name = input("Enter the updated name of user: ")
        phone = input("Enter the updated phone number of user: ")
        db1.update(id, name, phone)
    elif choice == 5:
        id = int(input("Enter the id of user: "))
        db1.delete(id)
    else:
        break