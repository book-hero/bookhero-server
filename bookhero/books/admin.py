from django.contrib import admin
from .models import Book, BookAttributes

# Register your models here.
admin.site.register(Book)
admin.site.register(BookAttributes)
