class Book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
    def __str__(self):
        return f"ID:{self.book_id},Title:{self.title},Author:{self.author}"