from django.db import models

from user.models import Person


class Property(models.Model):
    # class for many images in post
    image = models.ImageField(upload_to='users/posts/')


class Post(models.Model):
    # Post model for user`s profile
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    text = models.TextField(max_length=1500)
    images = models.ForeignKey(Property, blank=True, on_delete=models.PROTECT, null=True, )
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=1)
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='return_posts',)
    where_published = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='where_published',)

