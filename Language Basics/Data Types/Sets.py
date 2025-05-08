# Sets are used in those scenerios where we want to avoid the duplication of items when we are creating the collection of elements.

set1={1,"Ashok",3.5,0,3,"Bhatt",True,3}
# Sets are independent of order. Hence, on printing a set we might get the output in different orders.
print(set1)

# To create an empty set, we use built-in function set without any arguments, i.e. set()
# on lefting the curly brackets empty assigned to a variable i.e., x={} , we will get the dictionary data type
myset=set()
mydict={}
print("The data type of myset is {} and that of mydict is {}.".format(type(myset),type(mydict)))

# As indexing is not possible in set data type, we can access the list items using the "for loop"
# We cannot do so using while loop as it is independent of indexing or ordering
list_for={"Ashok",True,3,False,6,3,"Ashok"}
for i in list_for:
    print(i)

# All Set functions that helps us to perform the set operations:
set_1={1,4,2,5,2,6}
set_2={5,3,7,2,5}
print("The set_1 is given by:",set_1)
print("The set_2 is given by:",set_2)
print("The union of the set_1 and set_2 is given by:",set_1.union(set_2))
print("The intersection of the set_1 and set_2 is given by:",set_1.intersection(set_2))
print("The symmetric difference of the set_1 and set_2 is given by:",set_1.symmetric_difference(set_2))
print("The difference between the set_1 and set_2 is given by:",set_1.difference(set_2))
print("The difference between the set_2 and set_1 is given by:",set_2.difference(set_1))

# To represent set A as the the result obtained on performing the operation between set A and set B:
set_1.update(set_2)
print("set_1 as the union of set_1 and set_2:",set_1)

# If two sets are equal then they are subset as well as superset of each other
a={1,3,2,4,2}
b={1,2,3,4}
print("Is a subset of b:",a.issubset(b))
print("Is a superset of b:",a.issuperset(b))

# Discard- Error Free
# Remove- Raises Error if no element if found
# Pop- removes a random element
# del- deletes the entire existence of a set along with a variable
# clear- deletes the entire existence of a set without deleting the existence of a variable
a.remove(3)
a.discard(30)       # no error instead of no instance of 30 in set a
print(a)
a.pop()
print(a)
b.clear()
print("After clearing the set b, it is given by:",b)