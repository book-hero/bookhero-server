from books.models import Book, Author
from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import BookSerializer
from books.services import get_open_library_book_info


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookSerializer
