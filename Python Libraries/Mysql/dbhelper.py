import mysql.connector as connector

class DBHelper:

    def __init__(self):

        self.con = connector.connect(host="localhost", 
                                     port="3306", 
                                     user="root", 
                                     password="", 
                                     database="projects")
        
        query = "create table if not exists user(userId int primary key, userName varchar(30), phone varchar(10))"
        cur = self.con.cursor()
        cur.execute(query)
        print("Bann gaya table")


    def insert(self, id, name, phone):

        query = f"insert into products values({id}, '{name}', '{phone}')"
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()


    def fetch_all(self):

        query = f"select * from user"
        cur = self.con.cursor()
        cur.execute(query)

        try:
            print("\nData of all users:")
            for data in cur:
                id = data[0]
                name = data[1]
                phone = data[2]
                print(f"{id:<20}{name:<20}{phone:<20}")
        except:
            print("No data present!")

    
    def fetch_user_info(self, id):

        query = f"select * from user where userId={id}"
        cur = self.con.cursor()
        cur.execute(query)

        try:
            print("\nData of User:")
            for data in cur:
                id = data[0]
                name = data[1]
                phone = data[2]
                print(f"{id:<20}{name:<20}{phone:<20}")
        except:
            print(f"User with id={id} not present!")

    
    def update(self, id, name, phone):
        
        try:
            query = f"update user set userName='{name}', phone='{phone}' where userId={id}"
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
        except:
            print(f"User with id={id} not present!")

    
    def delete(self, id):
        
        try:
            query = f"delete from user where userId={id}"
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
        except:
            print(f"User with id={id} not present!")


if __name__=="__main__":
    helper = DBHelper()