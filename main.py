from datetime import datetime
from library import Library
from book import Book



library=Library(start_time=datetime.strptime("08:00","%H:%M").time(),
                end_time=datetime.strptime("18:00","%H:%M").time()
                )
book1=Book(1,'1984','George Orwell')
book2=Book(2,'To Kill a Mockingbird','Harper lee')
book3=Book(3,'The Great Gatsby','F.Scott Fitzgerald')

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_book()

print(library.search_book("1984"))
library.remove_book(2)

library.display_book()


if library.is_open():
    print('libraty is open')
else:
    print('library is closed')