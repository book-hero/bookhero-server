from rest_framework import serializers
from .models import UserBook, Profile, UserBookStatus
from books.models import Book
from books.serializers import BookSerializer
from attributes.models import AttributeDescriptor


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


class FinishBookSerializer(serializers.Serializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset=UserBook.objects.all()
    )
    selected_descriptor = serializers.PrimaryKeyRelatedField(
        queryset=AttributeDescriptor.objects.all()
    )
    status = serializers.PrimaryKeyRelatedField(
        queryset=UserBookStatus.objects.all()
    )
