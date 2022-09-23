class Library:
    def __init__(self, booksList, name):
        self.booksList = booksList
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f'We have following books in our library: {self.name}')
        for book in self.booksList:
            print(book)

    def addBook(self, book):
        if book in booksList:
            print('Book already exists')
        else:
            booksList.append(book)
            bookDatabase = open(databaseName, 'a')
            bookDatabase.write('\n')
            bookDatabase.write(book)
            print('Book added')

    def lendBook(self, book, user):
        if book in booksList:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print('Book has been added lended. Database updated.')
            else:
                print(f'Book is already being used by {self.lendDict[book]}')
        else:
            print('Apologies! We dont have this book in our library')

    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print('Book Returned Successfully')
        else:
            print('The book does not exists in the Book Lending Database')


def main():
    while True:
        print(f'Welcome to the {library.name} library. Following are the options,')
        choice = '''
        1. Display Books
        2. Lend a Book
        3. Add a Book
        4. Return a Book
        '''
        print(choice)
        userInput = input('Pess Q to quite and C to continue:')
        if userInput == 'C':
            userChoice = int(input('Select and option to continue:'))
            if userChoice == 1:
                library.displayBooks()

            elif userChoice == 2:
                book = input('Enter the name of the book you want to lend:')
                user = input('Enter the name of the user:')
                library.lendBook(book, user)

            elif userChoice == 3:
                book = input('Enter the name of the book you want to add:')
                library.addBook(book)

            elif userChoice == 4:
                book = input('Enter the name of the book you want to return:')
                library.returnBook(book)
            else:
                print('Please choose a valid option')
        elif userInput == 'Q':
            break

        else:
            print('Please enter a valid option')


if __name__ == '__main__':
    booksList = []
    # databaseName = input('Enter the name of the database file with extension:')
    databaseName = 'pythonxDatabase.txt'
    bookDatabase = open(databaseName, 'r')
    for book in bookDatabase:
        booksList.append(book.removesuffix('\n'))
    library = Library(booksList, 'PythonX')
    main()
    bookDatabase.close()
