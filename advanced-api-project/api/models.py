from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    # Model to represent an author with a name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Model to represent a book with a title, publication year, and a foreign key to an author
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title