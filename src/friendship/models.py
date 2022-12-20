from django.db import models

from user.models import Person

class Friendship(models.Model):
    from_user = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name='Sender')
    to_user = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name='Receiver')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return f"{self.person_id} wants to be your friend!"

    def return_time_created(self):
        return f"This application has been sent at {self.time_created}"



