from django.db import models
from django.contrib.auth.models import User
class Author(models.Model):
    name = models.CharField(max_length=50)

    def str(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length= 100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')

    def str(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def str(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete= models.CASCADE)

    def str(self):
        return self.name
    
    


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.user.username} - {self.role}'

