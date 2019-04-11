from .models import UserBook, UserBookStatus, Profile
from books.models import Book, Author
from rest_framework import viewsets, permissions
from .serializers import UserBookSerializer
from books.serializers import BookSerializer


class UserBookViewSet(viewsets.ModelViewSet):
    serializer_class = UserBookSerializer

    def get_queryset(self):
        return UserBook.objects.filter(profile=self.request.user.profile.id).all()

    def create(self, request):
        request.data['profile'] = request.user.profile.id
        return super(UserBookViewSet, self).create(request)
