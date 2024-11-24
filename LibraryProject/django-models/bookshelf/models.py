from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    


#Creating New Book
book = Book.objects.create(
    title="1984", 
    author="George Orwell", 
    publication_year=1949
)

#Output: """
# Successfully added: 1984,George Orwell,1949 to Books Table
# """

# Retrieving all books
Show_books = Book.objects.get()

#Output: """
# title |    author     | publication_year
#  1984   George Orwell      1949
# """


#Updating book title from 1984 to Nineteen Eighty-Four
update_title = Book.objects.get(title= "1984")
update_title.title = "Nineteen Eighty-Four"
update_title.save()

#Output: """
#        title         |    author     | publication_year
#  Nineteen Eighty-Four   George Orwell      1949
# """



#Deleting Book Named Nineteen Eighty-Four
del_book= Book.objects.get(title= 'Nineteen Eighty-Four')
del_book.delete()

# Output:
# Successfully deleted 'Nineteen Eighty-Four' from Books Table
# """
#Output: """
# title |    author     | publication_year
#  NULL       NULL            NULL
# """