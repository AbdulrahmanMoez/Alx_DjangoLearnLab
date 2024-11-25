from django.db import models
from .models import Book, Author, Library, Librarian

author = Author.objects.get(name=author_name)
author = Author.objects.filter(author=author)
library_books = Library.books.all()


library = Library.objects.get(name=library_name)  
librarian = library.librarian

# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.