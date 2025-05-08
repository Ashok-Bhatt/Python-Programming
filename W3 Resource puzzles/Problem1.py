# Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.

list1 = list(map(int, input("Please enter the list items separated by comma:").split(",")))
print("Entered List:",list1)

if (list1.count("19")==2) and (list1.count("5")>=3):
    print("Well Done Bro! condition satisfied!")
else:
    print("No Bro! Given list should contain exactly two occurrences of nineteen and at least three occurrences of five.")