class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__available_copies = available_copies

    def display_book(self):
        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, "
            f"Available Copies: {self.__available_copies}")

    def borrow_book(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            print(f"Book '{self.__title}' borrowed successfully. ")
            print(f"Available count is :{self.__available_copies}")
        else:
            print(f"Sorry, '{self.__title}' is not available right now.")

    def return_book(self):
        self.__available_copies += 1
        print(f"Book '{self.__title}' returned successfully.")
        print(f"Available count is :{self.__available_copies}")


    def get_title(self):
        return self.__title


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.get_title()}' added to the library.")

    def search(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                print("Book Found:")
                book.display_book()
                return book
        print("Book not found.")
        return None

    def display_all_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\n----- Library Books -----")
            for book in self.books:
                book.display_book()
            print("-------------------------\n")


if __name__ == "__main__":
    library = Library()

    library.add_book(Book(101, "kayar", "basheer", 3))
    library.add_book(Book(102, "it's start with us", "coollen hover", 2))
    library.add_book(Book(103, "fourty rule of love", "elif shafak", 1))

    while True:
        print("\n===== Library Menu =====")
        print("1. View All Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Search a Book by Title")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            library.display_all_books()

        elif choice == 2:
            title = input("Enter book title to borrow: ")
            book = library.search(title)
            if book:
                book.borrow_book()

        elif choice == 3:
            title = input("Enter book title to return: ")
            book = library.search(title)
            if book:
                book.return_book()

        elif choice == 4:
            title = input("Enter book title to search: ")
            library.search(title)

        elif choice == 5:
            print("Thank you for using the Library System!")
            break

        else:
            print("Invalid option! Please try again.")
