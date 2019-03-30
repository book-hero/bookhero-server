from .models import UserBook
from rest_framework import viewsets, permissions
from .serializers import UserBookSerializer


class UserBookViewSet(viewsets.ModelViewSet):
    # queryset = UserBook.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserBookSerializer

    def get_queryset(self):
        return self.request.user.books.all()
