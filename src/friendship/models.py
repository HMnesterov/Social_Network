from django.db import models

from user.models import Person


class Friendship(models.Model):
    from_user = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Sender',
                                     related_name='from_one_user')
    to_user = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Receiver',
                                   related_name='to_another_user')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return f"{self.from_user} wants to be your friend!"

    def return_time_created(self):
        return f"This application has been sent at {self.time_created}"

    def get_sender_id(self):
        return self.from_user.pk

    def get_receiver_id(self):
        return self.to_user.pk
