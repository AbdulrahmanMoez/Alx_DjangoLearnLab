from django.db import models
from .models import Book, Author, Library, Librarian

author = Author.objects.get(name = 'author_name')

library_books = Library.books.all()


Library.objects.get(name="library_name")
Librarian.objects.get(name="Librarian_name")

# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.