from django.contrib import admin
from django.urls import re_path, path, include
from django.views.generic import TemplateView
from frontend import views

# regex = re.compile(r'(?!\bapi\b|\badmin\b).*\/?')
urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('books.urls')),
    path('', include('attributes.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^(?P<path>.*)/$', views.index),
]
