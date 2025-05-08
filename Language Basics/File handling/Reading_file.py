myfile=open("./mytext.txt","r")        # "r" is the default file operation mode
txt1=myfile.read(5)
print("txt1=",txt1)
txt2=myfile.read()
print("txt2=",txt2)
myfile.close()

# We can open and close the file simultaneously by using the with statement
with open("../mytext.txt","r") as myfile:
    print(myfile.read())