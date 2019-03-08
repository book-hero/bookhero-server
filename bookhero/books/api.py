from books.models import Book
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
        ol_book = get_open_library_book_info("0575097345")
        book = Book(title=ol_book.title, publish_date=ol_book.publish_date,
                    open_library_url=ol_book.url)

        # get author id, and if they don't exist, create them.

        # get subject id, and create if not exist

        # make sure book doesn't already exist, and then add it with references to subjects and author(s)

        return Response({'status': 'success'})
