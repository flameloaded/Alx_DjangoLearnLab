from relationship_app.models import Author, Book, Library, Librarian

# Create or get Author
author_name = "Chinua Achebe"
author, created = Author.objects.get_or_create(name=author_name)

# Create or get Books
book_titles = ["Things Fall Apart", "No Longer at Ease"]
books = []
for title in book_titles:
    book, _ = Book.objects.get_or_create(title=title, author=author)
    books.append(book)

# Create or get Library
library_name = "Central Library"
library, _ = Library.objects.get_or_create(name=library_name)
library.books.set(books)  # Set books in the library

# Create or get Librarian
librarian_name = "John Doe"
Librarian.objects.get_or_create(name=librarian_name, library=library)

# 1. Query all books by a specific author
print(f"Books by {author_name}:")
for book in Book.objects.filter(author__name=author_name):
    print(f"- {book.title}")

# 2. List all books in a library
print(f"\nBooks in {library_name}:")
library = Library.objects.get(name=library_name)
for book in library.books.all():
    print(f"- {book.title}")

# 3. Retrieve the librarian for a library
librarian = library.librarian
print(f"\nLibrarian for {library_name}: {librarian.name}")

