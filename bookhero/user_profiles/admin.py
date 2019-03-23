from django.contrib import admin
from .models import UserBookStatus, UserBook, UserProfile

# Register your models here.
admin.site.register(UserBookStatus)
admin.site.register(UserBook)
# admin.site.register(UserProfile)
