# Deleting Book Named Nineteen Eighty-Four

from bookshelf.models import Book
del_book= Book.objects.get(title= 'Nineteen Eighty-Four')
del_book.delete()

""" #Output:
title |    author     | publication_year
NULL       NULL            NULL
"""
