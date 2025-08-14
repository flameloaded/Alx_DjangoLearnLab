from django.db import models

"""
Models overview
---------------
Author:
  - Represents a single author by name.
Book:
  - Represents a book with a title and the publication year.
  - Linked to an Author via a ForeignKey (one Author -> many Books).

Why related_name='books'?
  - Makes reverse access intuitive (author.books.all()) and
    simplifies nested serialization with DRF.
"""

class Author(models.Model):
    # Author's display name (unique not required for demo)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=255)
    # Publication year as integer (e.g., 2021)
    publication_year = models.IntegerField()
    # One-to-many: one Author can have many Books
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",  # enables author.books in code & serializers
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
