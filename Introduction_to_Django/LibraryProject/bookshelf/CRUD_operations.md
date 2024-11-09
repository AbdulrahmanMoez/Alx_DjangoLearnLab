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

Show_books = Book.objects.all()

""" #Output:
title |    author     | publication_year
1984   George Orwell      1949
"""

## Updating book title from 1984 to Nineteen Eighty-Four

update= Book.objects.filter(title= 1984).update(title='Nineteen Eighty-Four')
""" #Output:
       title         |    author     | publication_year
 Nineteen Eighty-Four   George Orwell      1949
"""

## Deleting Book Named Nineteen Eighty-Four

delete= Book.objects.filter(title= 'Nineteen Eighty-Four').delete()
""" #Output:
title |    author     | publication_year
NULL       NULL            NULL
"""
