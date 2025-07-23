from relationship_app.models import Author, Book, Library, Librarian

# 1. Get or create the author
author_name = "Chinua Achebe"
try:
    author = Author.objects.get(name=author_name)  # required pattern
except Author.DoesNotExist:
    author = Author.objects.create(name=author_name)

# 2. Create or get books by the author
book_titles = ["Things Fall Apart", "No Longer at Ease"]
books = []
for title in book_titles:
    book, _ = Book.objects.get_or_create(title=title, author=author)
    books.append(book)

# 3. Get or create the library
library_name = "Central Library"
library, _ = Library.objects.get_or_create(name=library_name)
library.books.set(books)

# 4. Get or create the librarian
librarian_name = "John Doe"
Librarian.objects.get_or_create(name=librarian_name, library=library)

# === Sample Queries ===

# Query all books by a specific author
print(f"Books by {author_name}:")
books_by_author = Book.objects.filter(author=author)  # required pattern
for book in books_by_author:
    print(f"- {book.title}")

# List all books in a library
print(f"\nBooks in {library_name}:")
for book in library.books.all():
    print(f"- {book.title}")

# Retrieve the librarian for a library using Librarian.objects.get(library=...)
librarian = Librarian.objects.get(library=library)  # required pattern
print(f"\nLibrarian for {library_name}: {librarian.name}")
