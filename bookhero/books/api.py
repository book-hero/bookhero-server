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

    def create(self, request):
        # get or make the author objects
        authors = []
        for author in request.data['authors']:
            existing_author, created = Author.objects.get_or_create(
                name=author)
            authors.append(existing_author.id)
        request.data['authors'] = authors

        # get applicable attribute ids

        return super(BookViewSet, self).create(request)
