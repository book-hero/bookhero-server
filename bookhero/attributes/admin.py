from django.contrib import admin
from .models import Attribute, AttributeDescriptor

# Register your models here.
admin.site.register(Attribute)
admin.site.register(AttributeDescriptor)
