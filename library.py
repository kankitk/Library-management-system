import os

class Library:
    def __init__(self, listofbooks, libraryname):
        self.listofBooks = listofbooks
        self.libraryName = libraryname
        self.lenders={}

    def displayBook(self):
        print (self.listofBooks)

    def lendBook(self, personeName, bookName):
        if bookName in self.listofBooks:
            if personeName in self.lenders.items():
                self.lenders[personeName].append(bookName)
            else:
                self.lenders[personeName] = [bookName]

            self.listofBooks.remove(bookName)
            print("Book has been issued")
        else:
            if self.lenders:
                for i, j in self.lenders:
                    if bookName in j:
                        print(f"this book is not available in library, currently it is owned by {i}\n")
            else:
                print("this book is not present in our library\n")


    def addBook(self, bookName):
        self.listofBooks.append(bookName)
        print("the book is added successfully, thank you")

    def returnBook(self, personeName, bookName):
        self.lenders[personeName].remove(bookName)
        self.listofBooks.append(bookName)
        if self.lenders[personeName]:
            pass
        else:
            del self.lenders[personeName]


A=Library(['java', 'c++', 'c', 'data structre'], 'Ankit')

while True:
    inp= input(f"\n\nWelcome to {A.libraryName} library\n\n"
               "1 - Display books\n"
               "2 - Lend Book\n"
               "3 - Add Book\n"
               "4 - Return Book\n"
               "5 - Exit\n"
               "\n\nEnter your choice here:- ")
    if inp == '1':
        A.displayBook()
    elif inp == '2':
        pname = input("Enter your name: ")
        bname = input("Enter bookk name: ")
        A.lendBook(pname,bname)
    elif inp == '3':
        bname = input("Enter book name: ")
        A.addBook(bname)
    elif inp == '4':
        pname = input("Enter your name: ")
        bname = input("Enter book name: ")
        A.returnBook(pname,bname)
    elif inp == '5':
        break
    else:
        print("Invalid input, please try again")
