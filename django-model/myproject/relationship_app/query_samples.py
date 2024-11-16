from relationship_app.models import Author, Book, Library, Librarian

author_name = Author.objects.get(name='Sharon')
Author.objects.get(name=author_name)

books = Book.objects.all()
books.all()

library_name = 'Sharon Muingo Library'
library = Library.objects.get(name=library_name)
Librarian.objects.get(library=library)