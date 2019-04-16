from rest_framework import serializers
from attributes.models import Attribute, AttributeDescriptor


class AttributeDescriptorSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttributeDescriptor
        fields = '__all__'


class AttributeSerializer(serializers.ModelSerializer):
    descriptors = AttributeDescriptorSerializer(read_only=True, many=True)
    # descriptors = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Attribute
        fields = '__all__'
