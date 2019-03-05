from attributes.models import Attribute
from rest_framework import viewsets, permissions
from .serializers import AttributeSerializer

# Book Viewset


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AttributeSerializer
