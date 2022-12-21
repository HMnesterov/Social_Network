from django.db import models


class Property(models.Model):
    # class for many images in post
    image = models.ImageField(upload_to='users/posts/')


class Post(models.Model):
    # Post model for user`s profile
    created_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1500)
    images = models.ForeignKey(Property, blank=True, on_delete=models.PROTECT, null=True, )


