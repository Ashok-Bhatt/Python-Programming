class vertebrata:
    hasBone = True

class mammal(vertebrata):
    giveEggs = False

class lion(mammal):
    name = "Lion"
    scientificName = "Panthera leo"
    length = 1.8
    weigth = 200

class tiger(mammal):
    name = "Tiger"
    scientificName = "Panthera Tigris"
    length = 2.5
    weigth = 150

tiger1 = tiger()
print(tiger1.name)
print(tiger1.hasBone)
print(tiger1.giveEggs)
print(tiger1.scientificName)
print(tiger1.length)
print(tiger1.weigth)

print("")

lion1 = lion()
print(lion.name)
print(lion1.hasBone)
print(lion1.giveEggs)
print(lion1.scientificName)
print(lion1.length)
print(lion1.weigth)