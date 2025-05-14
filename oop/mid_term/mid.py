class Library:
    book_list = []

    @classmethod
    def entry_book(self, book):
        self.book_list.append(book)

    @classmethod
    def view_all_books(self):
        if self.book_list:
            for book in self.book_list:
                book.view_book_info()
                print() 
        else:
            print("No books available")


class Book:
    def __init__(self, book_id, title, author, availability):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"You borrowed '{self.__title}' ")
        else:
            print(f"'{self.__title}' is not available")

    def return_book(self):
        self.__availability = True
        print(f"You returned '{self.__title}'")

    def view_book_info(self):
        print(f'Book ID: {self.__book_id}')
        print(f'Title: {self.__title}')
        print(f'Author: {self.__author}')
        print(f'{'Available' if self.__availability else 'Not Available'}')
        print()
    
    def get_book_id(self):
        return self.__book_id


Book1 = Book(101, 'The Prince', 'Niccolo Machiavelli', True)
Book2 = Book(102, '1984', 'George Orwell', False)
Book2 = Book(103, '48 Laws of Power', 'Robert Greene', True)

# Book1.view_book_info()
# Book2.view_book_info()

# for book in Library.book_list:
#     print(f'{book.book_id}: {book.title} by {book.author} - {'Available' if book.availability else 'Not Available'} ')

while True:
    print('-------- Library Menu --------')
    print('1. View All Books')
    print('2. Borrow Books')
    print('3. Return Books')
    print('4. Exit')
    choice = input('Enter Choice: ')

    if choice == '1':
        Library.view_all_books()

    elif choice == '2':
        try:
            book_id = int(input("Enter book ID to borrow: "))
            found = False
            for book in Library.book_list:
                if book.get_book_id() == book_id:
                    book.borrow_book()
                    found = True
                    break
            if not found:
                print("Book not found.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '3':
        try:
            book_id = int(input("Enter book ID to return: "))
            found = False
            for book in Library.book_list:
                if book.get_book_id() == book_id:
                    book.return_book()
                    found = True
                    break
            if not found:
                print("Book not found.")
        except ValueError:
            print("Please enter a valid number.")
            
    elif choice == '4':
        print("Exiting Library System.")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
