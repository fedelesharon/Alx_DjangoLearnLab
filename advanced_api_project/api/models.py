from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Author(models.Model):
    """
    Represents an author who can write multiple books.
    Fields:
    - name: Stores the author's name.
    """
    ...

class Book(models.Model):
    """
    Represents a book with its title, publication year, and author relationship.
    Fields:
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: Foreign key linking the book to an Author.
    """
    ...
