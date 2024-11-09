# Creating New Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

"""
Output:
Successfully added: 1984, George Orwell, 1949 to Books Table
"""

## Retrieving all books

book = Book.objects.get()

""" #Output:
title |    author     | publication_year
1984   George Orwell      1949
"""

## Updating book title from 1984 to Nineteen Eighty-Four

book = Book.objects.get(title= "1984")
book.title = "Nineteen Eighty-Four"
book.save()

""" #Output:
       title         |    author     | publication_year
 Nineteen Eighty-Four   George Orwell      1949
"""

## Deleting Book Named Nineteen Eighty-Four

from bookshelf.models import Book
book= Book.objects.get(title= 'Nineteen Eighty-Four')
book.delete()

""" #Output:
title |    author     | publication_year
NULL       NULL            NULL
"""
