from django.db import models

from user.models import Person


class Notification(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='notifications')
    text = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text


