# Without Enumerate:
fruits=["Mango","Apple","Banana"]
index=0
for fru in fruits:
    print(index,fru)
    index+=1

# With Enumerate:
vegetables=["Potato","Tomato","Brinjal"]
for index,veg in enumerate(vegetables):
    print(index,veg)

marks=[70,78,82]
for index,mark in enumerate(marks,start=1):
    print(index,mark)