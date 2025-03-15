class Book:
    def __init__(self, title, author, available = True):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        # Use lambda to search for books by title
        search_title = lambda book: book.title.lower() == title.lower()
        return list(filter(search_title, self.books))

    def search_by_author(self, author):
        # Use lambda to search for books by author
        search_author = lambda book: book.author.lower() == author.lower()
        return list(filter(search_author, self.books))

    def update_availability(self, title, available):
        # Use lambda to update book availability
        update_book = lambda book: setattr(book, "available", available) if book.title.lower() == title.lower() else None
        list(map(update_book, self.books))

# Create instances of the Book class
book1 = Book("Lord of the Rings, Fellowship of the Ring", "J.R.R Tolkien")
book2 = Book("Harry Potter, The Philosophers Stone", "J.K Rowling")
book3 = Book("Bartimaeus, The Amulet of Samarkand","Jonathan Stroud")

# Create an instance of the Library class
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Search for books by title
print(" Books with title  'Lord of the Rings, Fellowship of the Ring':")
for book in library.search_by_title("Lord of the Rings, Fellowship of the Ring"):
    print(f" - {book.title} by {book.author}")

# Search for books by author
print("\nBooks by author 'J.R.R Tolkien':")
for book in library.search_by_author("J.R.R Tolkien"):
    print(f" - {book.title} by {book.author}")

# Update book availability
library.update_availability("Harry Potter, The Philosophers Stone", False)

# Check updated availability
print("\nAvailability of 'Harry Potter, The Philosophers Stone':")
for book in library.search_by_author("Harry Potter, The Philosophers Stone"):
    print(f" - {book.title} is {'available' if book.available else 'not available'}")





