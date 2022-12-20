from django.contrib.auth.models import AbstractUser
from django.db import models




class Person(AbstractUser):
    photo = models.ImageField(blank=True, upload_to='media/users/users_main_photos/',
                              default='media/users/users_main_photos/default.jpg')
    friends = models.ManyToManyField('self', blank=True, verbose_name='friends', related_name='fr', symmetrical=False)

    bio = models.TextField(max_length=200, default='Not stated', blank=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.username