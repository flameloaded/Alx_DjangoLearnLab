from datetime import date
from rest_framework import serializers
from .models import Author, Book

"""
Serializer overview
-------------------
BookSerializer:
  - Serializes all Book fields.
  - Adds custom validation to ensure publication_year is not in the future.

AuthorSerializer:
  - Serializes author's name.
  - Includes a nested list of books using BookSerializer(many=True).
  - Uses the related_name='books' from Book.author to pull related books.

Relationship handling:
  - The Author -> Book one-to-many is surfaced via Author.books
    (thanks to related_name). In AuthorSerializer, we expose it as
    'books' using BookSerializer(many=True, read_only=True).

Note:
  - If you want to allow creating/updating books inline within the author
    payload, you'd drop read_only=True and implement create()/update()
    to handle nested writes. Here we keep it read-only for clarity.
"""

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "publication_year", "author"]

    def validate_publication_year(self, value):
        # Ensure the publication year is not in the future
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year {value} cannot be in the future (>{current_year})."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    # Pull related books via 'books' related_name (read-only nested)
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
