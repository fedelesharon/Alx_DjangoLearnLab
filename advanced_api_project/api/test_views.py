# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a sample book for testing
        self.book = Book.objects.create(title='Test Book', author='Test Author', publication_year=2021)

    def test_create_book(self):
        """Test creating a book."""
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2022}
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_books(self):
        """Test retrieving the list of books."""
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return the initial book

    def test_get_book_detail(self):
        """Test retrieving a specific book by ID."""
        response = self.client.get(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        """Test updating a book."""
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': 2023}
        response = self.client.put(reverse('book-update', args=[self.book.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        """Test deleting a book."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(reverse('book-delete', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        """Test filtering books by title."""
        response = self.client.get(reverse('book-list') + '?title=Test Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """Test searching books by title."""
        response = self.client.get(reverse('book-list') + '?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        """Test ordering books by publication year."""
        response = self.client.get(reverse('book-list') + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_unauthenticated(self):
        """Test creating a book without authentication."""
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2022}
        response = self.client.post(reverse('book-create'), data)
       