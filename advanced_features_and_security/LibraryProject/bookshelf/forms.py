# LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book  # or any model you're working with

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']  # adjust based on your Book model fields
