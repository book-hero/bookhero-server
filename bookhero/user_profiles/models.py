from django.db import models
from bookhero.models import TimeStamped
import attributes.models
import books.models
from users.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserBookStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Profile(TimeStamped):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    books = models.ManyToManyField('books.Book', through="UserBook")
    attributes = models.ManyToManyField(
        'attributes.Attribute', through="UserAttribute")

    def __str__(self):
        return self.user.email


class UserBook(TimeStamped):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.ForeignKey(UserBookStatus, on_delete=models.CASCADE)
    started = models.DateTimeField(null=True)
    date_finished = models.DateTimeField(null=True)


class UserAttribute(TimeStamped):
    attribute = models.ForeignKey(
        'attributes.Attribute', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    value = models.IntegerField(null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
