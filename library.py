from datetime import datetime
from book import Book

class Library:
    def __init__(self,start_time,end_time):
        self.collection=[]
        self.total_books=0
        self.start_time=start_time
        self.end_time=end_time
    def add_book(self,book):
        """add a book to the collection"""
        self.collection.append(book)
        self.total_books += 1
        print(f"book'{book.title}'added to the library.")
    def remove_book(self,book_id):
        """remove the book by id"""
        for book in self.collection:
            if book.book_id==book_id:
                self.collection.remove(book)
                self.total_books -= 1
                print(f"Book'{book.title}'removed from library.")
                return
        print("Book not found.")
    def search_book(self,title):
        """search for a book by title"""
        for book in self.collection:
            if book.title.lower() == title.lower():
                return book
        return 'Book not found'
    def display_book(self):
        """display add books in the library"""
        if not self.collection:
            print('No books in the library.')
        else:
            print('Books in the library.')
            for book in self.collection:
                print(book)
    def is_open(self):
        """check if the library is open"""
        current_time=datetime.now().time()
        return self.start_time <= current_time <= self.end_time
