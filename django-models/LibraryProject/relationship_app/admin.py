from django.contrib import admin

from django.contrib import admin
from .models import Book, Author, Library, Librarian

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)
