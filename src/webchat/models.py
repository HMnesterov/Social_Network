from django.db import models
from user.models import Person



class Chat(models.Model):
    title = models.CharField(max_length=60)
    members = models.ManyToManyField(Person, blank=True)

class Message(models.Model):
    text = models.CharField(max_length=500)
    author = models.ForeignKey(Person, related_name='messages', on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_messages')

    def __str__(self):
        return f"{self.author}: {self.text}"





