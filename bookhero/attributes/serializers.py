from rest_framework import serializers
from attributes.models import Attribute

# Book Serializer


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'
