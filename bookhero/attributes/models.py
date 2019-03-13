from django.db import models
from bookhero.models import TimeStamped


class Attribute(TimeStamped):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name
