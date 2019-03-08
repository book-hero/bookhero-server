from django.contrib import admin
from .models import Book, BookAttribute, IdentifierType, Subject, Author

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookAttribute)
admin.site.register(IdentifierType)
admin.site.register(Subject)
