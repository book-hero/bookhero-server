from django.contrib import admin
from django.urls import re_path, path, include
from django.views.generic import TemplateView

# regex = re.compile(r'(?!\bapi\b|\badmin\b).*\/?')
urlpatterns = [
    path('', include('books.urls')),
    path('', include('attributes.urls')),
    path('admin/', admin.site.urls),
]
