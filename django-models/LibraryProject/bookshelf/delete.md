# Deleting Book Named Nineteen Eighty-Four

from bookshelf.models import Book
book= Book.objects.get(title= 'Nineteen Eighty-Four')
book.delete()

""" #Output:
title |    author     | publication_year
NULL       NULL            NULL
"""
