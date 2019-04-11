from django.contrib import admin
from .models import UserBookStatus, UserBook

# Register your models here.
admin.site.register(UserBookStatus)
admin.site.register(UserBook)
