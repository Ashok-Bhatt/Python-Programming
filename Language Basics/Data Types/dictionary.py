# Dictionaries are ordered collection from python 3.7 onwards
cartoon={"Shinchan":"Japan","Pokemon":"Japan","Ben 10":"USA"}
print(cartoon)

# Throws an error
print(cartoon["Shinchan"])
# Doesn't throw any error
print(cartoon.get('Shinchan'))

# dict.keys()   : access all the keys
# dict.values() : access all the values
# dict.items()  : access all the key-value pairs
print("The keys in a given dictionary are:",cartoon.keys())
print("The values in a given dictionary are:",cartoon.values())
print("The key-value pairs in a given dictinary are:",cartoon.items())

# Do not forgot to place a small brackets after cartoon.keys()
for keys in cartoon.keys():
    print("The value corresponding to key {} is: {}".format(keys,cartoon[keys]))
for key,value in cartoon.items():
    print("The value corresponding to key {} is: {}".format(key,value))

# using method a.update(b), all elements from the b gets transferred to a but remains in b also
animal1={"Lion":"Carnivores","Rabbit":"Herbivores","Chimpanzee":"Herbivores","Tiger":"Carnivores"}
animal2={"Bear":"Omnivores","Deer":"Herbivores"}
animal1.update(animal2)
print("animal1=",animal1)
print("animal2=",animal2)
animal2.clear()
print("animal2=",animal2)

# pop method is used to remove the desired key-value pair of the dictionary using the key name
# popitem method is used to remove the last key-value pair of the dictinary
animal1.pop("Lion")
print("animal1=",animal1)
animal1.popitem()
print("animal1=",animal1)