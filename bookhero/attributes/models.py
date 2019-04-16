from django.db import models
from bookhero.models import TimeStamped


class Attribute(TimeStamped):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    @property
    def descriptors(self):
        return self.descriptors.all()

    def __str__(self):
        return self.name


class AttributeDescriptor(TimeStamped):
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name='descriptors')
    descriptor = models.CharField(max_length=255)

    def __str__(self):
        return self.descriptor
