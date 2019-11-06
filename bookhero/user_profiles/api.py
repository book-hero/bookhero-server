from .models import Profile, UserAttribute, UserBook, UserBookStatus
from books.models import Book, Author, BookAttribute
from rest_framework import viewsets, permissions
from .serializers import UserBookSerializer, FinishBookSerializer
from books.serializers import BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone


class UserBookViewSet(viewsets.ModelViewSet):
    serializer_class = UserBookSerializer

    def get_queryset(self):
        return UserBook.objects.filter(profile=self.request.user.profile.id).all()

    def create(self, request):
        request.data['profile'] = request.user.profile.id
        return super(UserBookViewSet, self).create(request)

    def perform_update(self, serializer):
        if (serializer.validated_data["status"]
                == UserBookStatus.objects.get(id=2)):
            serializer.save(started=timezone.now())
        else:
            serializer.save()

    @action(methods=['post'], detail=True, url_path='finish')
    def finish_book(self, request, pk=None):
        data = request.data
        serializer = FinishBookSerializer(data=data)
        serializer.is_valid()
        user_book = serializer.validated_data['book']
        descriptor = serializer.validated_data['selected_descriptor']
        status = serializer.validated_data['status']

        # Update User Attribute
        user_attribute, created = UserAttribute.objects.get_or_create(
            profile=user_book.profile, attribute=descriptor.attribute)
        user_attribute.value = 1 if user_attribute.value == None else user_attribute.value + 1
        user_attribute.save()

        # Update Book Attribute
        book_attribute, created = BookAttribute.objects.get_or_create(
            book=user_book.book, attribute=descriptor.attribute)
        book_attribute.value = 1 if book_attribute.value == None else book_attribute.value + 1
        book_attribute.save()

        # Update Book Status
        user_book.status = status
        user_book.date_finished = timezone.now()
        user_book.save()

        return Response({'success': 'true'})
