from relationship_app.models import Author, Book, Library, Librarian

# Example data setup (optional)
author = Author.objects.create(name="Chinua Achebe")
book1 = Book.objects.create(title="Things Fall Apart", author=author)
book2 = Book.objects.create(title="No Longer at Ease", author=author)

library = Library.objects.create(name="Central Library")
library.books.set([book1, book2])  # Associate books with the library

librarian = Librarian.objects.create(name="John Doe", library=library)

# 1. Query all books by a specific author
author_books = Book.objects.filter(author__name="Chinua Achebe")
print("Books by Chinua Achebe:")
for book in author_books:
    print(f"- {book.title}")

# 2. List all books in a library
library_books = Library.objects.get(name="Central Library").books.all()
print("\nBooks in Central Library:")
for book in library_books:
    print(f"- {book.title}")

# 3. Retrieve the librarian for a library
librarian = Library.objects.get(name="Central Library").librarian
print(f"\nLibrarian of Central Library: {librarian.name}")
