from django.contrib.auth.models import AbstractUser
from django.db import models


class Friendship(models.Model):
    accepted = models.BooleanField(default=False)
    person_id = models.OneToOneField('Person', on_delete=models.CASCADE)



class Person(AbstractUser):
    photo = models.ImageField(blank=True, upload_to='media/users/users_main_photos/')
    friends = models.ManyToManyField('self', blank=True, null=True, verbose_name='friends', related_name='fr', on_delete=models.PROTECT)
    friends_requests = models.ForeignKey(Friendship, blank=True, null=True, verbose_name='friend_accept', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


