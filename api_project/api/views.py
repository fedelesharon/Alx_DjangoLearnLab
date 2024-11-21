from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

urlpatterns = [
    path('get_token/', obtain_auth_token, name='get_token'),
    ...
]
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]    