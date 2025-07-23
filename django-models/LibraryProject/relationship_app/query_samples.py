from relationship_app.models import Author, Book, Library, Librarian

# Create sample data only if not already existing

# 1. Get or create author
author_name = "Chinua Achebe"
try:
    author = Author.objects.get(name=author_name)
except Author.DoesNotExist:
    author = Author.objects.create(name=author_name)

# 2. Create books by the author if they don't exist
book_titles = ["Things Fall Apart", "No Longer at Ease"]
books = []
for title in book_titles:
    book, _ = Book.objects.get_or_create(title=title, author=author)
    books.append(book)

# 3. Get or create a library and assign books
library_name = "Central Library"
library, _ = Library.objects.get_or_create(name=library_name)
library.books.set(books)

# 4. Get or create librarian
librarian_name = "John Doe"
Librarian.objects.get_or_create(name=librarian_name, library=library)

# === Required Queries ===

# Query all books by a specific author using: objects.filter(author=author)
print(f"Books by {author_name}:")
author = Author.objects.get(name=author_name)  # <- required usage
books_by_author = Book.objects.filter(author=author)  # <- required usage
for book in books_by_author:
    print(f"- {book.title}")

# List all books in a library
print(f"\nBooks in {library_name}:")
library = Library.objects.get(name=library_name)
for book in library.books.all():
    print(f"- {book.title}")

# Retrieve the librarian for a library
librarian = library.librarian
print(f"\nLibrarian for {library_name}: {librarian.name}")
