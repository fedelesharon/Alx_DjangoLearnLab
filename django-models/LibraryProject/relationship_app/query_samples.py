from relationship_app.models import Author, Book, Library, Librarian

author_name = Author.objects.get(name='Mike')
Author.objects.filter(author=author)
books = Book.objects.all()
books.all()

library_name = 'Mike  Absai Library'
library = Library.objects.get(name=library_name)
Librarian.objects.get(library=library)