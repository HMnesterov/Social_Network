from django.contrib.auth.models import AbstractUser
from django.db import models


class Friendship(models.Model):
    accepted = models.BooleanField(default=False)
    person_id = models.OneToOneField('Person', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person_id} wants to be your friend!"



class Person(AbstractUser):
    photo = models.ImageField(blank=True, upload_to='media/users/users_main_photos/')
    friends = models.ManyToManyField('self', blank=True,  verbose_name='friends', related_name='fr',symmetrical=False)
    friends_requests = models.ForeignKey(Friendship, blank=True, null=True, verbose_name='friend_accept', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name



