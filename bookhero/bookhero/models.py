from django.db import models
from django.utils import timezone


class TimeStamped(models.Model):
    created = models.DateTimeField(default=timezone.now, editable=False)
    last_modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if 'update_fields' in kwargs and 'last_modifed' not in kwargs['update_fields']:
            kwargs['update_fields'].append('last_modified')

        self.last_modified = timezone.now()
        return super(TimeStamped, self).save(*args, **kwargs)

    class Meta:
        abstract = True
