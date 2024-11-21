from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register the viewset with it
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # API endpoint for book listing
    path('', include(router.urls)), 
]
