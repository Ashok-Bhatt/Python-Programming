#  Write a Python program to find all words in a given string with n consonants.

sentence=input("Enter the sentence (Do not use any number or symbol, just use english alphabet):")
list_words=sentence.split(" ")
dict_words={}

for i in list_words:
    list_consonant=[]
    for j in i:
        if (j not in "aeiou") and (j not in "AEIOU"):
            list_consonant.append(j)
            dict_words[i]=list_consonant

max_consonent=0
for occurances in dict_words.values():
    if len(occurances)>max_consonent:
        max_consonent=len(occurances)

# for i in range(1,max_consonent+1):
#     for values 