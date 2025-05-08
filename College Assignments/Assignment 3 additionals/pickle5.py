import pickle
import os

os.chdir("Assignment 3 additionals")

authors = []

class Book:
    def __init__(self, book_no, book_name, author, price):
        self.book_no = book_no
        self.book_name = book_name
        self.author = author
        self.price = price
        authors.append([self.book_no,self.book_name,self.author,self.price])
        
    def display_rec(self):
        with open("Books.dat", "rb") as filename:
            authors_list = pickle.load(filename)
            for i in authors_list:
                if str(i[0])==str(self.book_no):
                    print("Book No.:",i[0])
                    print("Book Name:",i[1])
                    print("Author:",i[2])
                    print("Price:",i[3])

    def count_rec(author):
        count = 0
        with open("Books.dat", "rb") as filename:
            authors_list = pickle.load(filename)
            for i in authors_list:
                if i[2]==author:
                    count = count + 1

        with open(f"{author}.dat", "wb") as f:
            pickle.dump(count, f)
            return count

book1 = Book(1, "Exam Warriors", "Narendra Modi", 250)
book2 = Book(2, "My Experiments with truth", "Mahatama Gandhi", 200)
book3 = Book(3, "Gitanjali", "Rabindranath Tagore", 150)

with open("Books.dat","wb") as filename:
    pickle.dump(authors,filename)

book1.display_rec()
book2.display_rec()
book3.display_rec()
print(Book.count_rec("Rabindranath Tagore"))