from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns shown in list view
    list_filter = ('author', 'publication_year')            # filters on the right
    search_fields = ('title', 'author')                     # search box fields
