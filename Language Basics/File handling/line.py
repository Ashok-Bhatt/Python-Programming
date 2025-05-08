file=open("./mytext.txt", "r")
contents = file.read()
lines = contents.split("\n")
print("Number of lines:", len(lines))
words = contents.split()
unique_words = set()
for word in words:
    unique_words.add(word)
print("Number of unique words:", len(unique_words))