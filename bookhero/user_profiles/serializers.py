from rest_framework import serializers
from .models import UserBook, Profile
from books.models import Book
from books.serializers import BookSerializer


class UserBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        write_only=True
    )

    class Meta:
        model = UserBook
        fields = '__all__'

    def create(self, validated_data):
        user_book = UserBook.objects.create(
            book=validated_data['book_id'], profile=validated_data['profile'], status=validated_data['status'])
        return user_book
