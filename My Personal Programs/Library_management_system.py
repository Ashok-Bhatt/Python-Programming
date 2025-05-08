class library:
     
    def __init__(self,list_books,no_books):
        self.lis=list_books
        self.num=no_books

    def check(self):
        if len(self.lis)==self.num:
            print("The total number of books in library is equal to the number of books currently present in the library.")
        elif len(self.lis)>self.num:
            print("The number of books currently present in the library is greater than the book capacity of the library.")
        else:
            print("Some of the books in library are missing.")
    
class library_engineering(library):
    def students(self):
        print("")

progm_lang=library_engineering(["Python","Javascript","C++","Java","SQL"],5)
progm_lang.check()
progm_lang.students()