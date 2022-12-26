from django.db import models
from config.settings import AUTH_USER_MODEL




class Message(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username


class Chat(models.Model):
    title = models.CharField(max_length=100)
    participants = models.ManyToManyField(AUTH_USER_MODEL, related_name='chats', blank=True)
    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return self.title



