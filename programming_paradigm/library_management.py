"""
our Task: library_management.py
Implement a Book class with public attributes title and author, 
and a private attribute _is_checked_out to track its availability.
Implement a Library class with a private list _books to store instances of 
Book. Include methods to add_book, check_out_book(title), 
return_book(title), and list_available_books.
Provided for Testing: main.py
This script demonstrates how to interact with your Book and Library classes.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

        
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"{self.title} by {self.author} has been checked out.")
        else:
            print(f"{self.title} by {self.author} is already checked out.")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"{self.title} by {self.author} has been returned.")
        else:
            print(f"{self.title} by {self.author} is already available.")

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        print(f"{book.title} by {book.author} has been added to the library.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
            #print(f"{title} is not available in the library")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"{title} is not available in the library")

    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"{book.title} by {book.author}")

        else:
            print("No books are available in the library")