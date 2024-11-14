import os
import django

# Set the environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')

# Initialize Django
django.setup()

from relationship_app.query_samples import get_books_by_author, list_books_in_library, get_librarian_for_library

# Example usage
books_by_author = get_books_by_author('Jane Austen')
print("Books by Jane Austen:", [book.title for book in books_by_author])

books_in_library = list_books_in_library('Central Library')
print("Books in Central Library:", [book.title for book in books_in_library])

librarian = get_librarian_for_library('Central Library')
print("Librarian of Central Library:", librarian.name)

