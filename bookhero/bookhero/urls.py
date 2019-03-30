from django.contrib import admin
from django.urls import path, include

# regex = re.compile(r'(?!\bapi\b|\badmin\b).*\/?')
urlpatterns = [
    path('', include('books.urls')),
    path('', include('attributes.urls')),
    path('', include('user_profiles.urls')),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
]
