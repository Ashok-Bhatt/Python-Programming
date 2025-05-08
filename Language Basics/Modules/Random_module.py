import random

# random function of random module can be used to get an random floating point value between 0 and 1
print("Random floating point value between 0 and 1",random.random())
print("Random floating point value between 0 and 1",random.random())
# We can also get a random floating point value between desired integers
print("Random floating point value between 0 and 100:",random.random()*100)
print("Random floating point value between 0 and 20:",random.random()*20)

# randint function of random module can be used to get a random integer between the integers passed in the arguments
print("The random integer between 1 and 10 is:",random.randint(1,10))
print("The random integer between 1 and 1 is:",random.randint(1,1))  # passing same value in the arguments leads to get the same value over and again

# animal contains a list of wild animal
animal=["Elephant","Lion","Tiger","Deer","Fox"]
print("The original list animal is given by:",animal)
for i in range(2):
    print("The randomly selected element from the list animal is:",random.choice(animal))
    random.shuffle(animal)
    print("The list animal after shuffling is given by:",animal)