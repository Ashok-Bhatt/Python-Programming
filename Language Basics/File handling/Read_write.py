with open("./Winners.txt","w") as myfile:
    list_winner=["Ashok","4","Sohan","5","Aman","6","Arijit","4"]
    for i in list_winner:
        myfile.write(f"{i}\n")

with open("../Winners.txt","r") as newfile:
    list_read=newfile.readlines()
    print(list_read)