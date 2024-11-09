# Updating book title from 1984 to Nineteen Eighty-Four

update_title = Book.objects.get(title= "1984")
update_title.title = "Nineteen Eighty-Four"
update_title.save()

""" #Output:
       title         |    author     | publication_year
 Nineteen Eighty-Four   George Orwell      1949
"""
