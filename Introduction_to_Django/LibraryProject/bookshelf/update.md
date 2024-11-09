# Updating book title from 1984 to Nineteen Eighty-Four

update_title = Book.objects.get(title= 1984)
book.title(title='Nineteen Eighty-Four')
book.save()

""" #Output:
       title         |    author     | publication_year
 Nineteen Eighty-Four   George Orwell      1949
"""
