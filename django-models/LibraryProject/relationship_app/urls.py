from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views as auth_views
from . import views
from . import views
urlpatterns = [
    path('books/', list_books, name = 'list_books'),
     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),  # URL for adding books
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # URL for editing books
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('add_book/', views.add_book, name='add_book'),  # URL for adding a book
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # URL for editing a book
]
