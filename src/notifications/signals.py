from django.db.models.signals import post_save
from django.dispatch import receiver

from friendship.models import Friendship
from notifications.models import Notification
from user_profile.models import Post
from webchat.models import Message


@receiver(signal=post_save, sender=Friendship)
def send_notification_to_message_receiver(sender, instance, created, *args, **kwargs):
    message = f"User {instance.from_user} wants to add you as a friend!"

    receiver_user = instance.to_user
    Notification.objects.create(user=receiver_user, text=message)




@receiver(signal=post_save, sender=Post)
def send_notification_to_page_owner_where_post_has_been_published(sender, instance, created, *args, **kwargs):
    author = instance.author
    page_owner = instance.where_published
    if author == page_owner:
        return
    message = f"User {author} published a post on your profile!"
    Notification.objects.create(user=page_owner, text=message)




@receiver(signal=post_save, sender=Message)
def send_notification_to_chat_members_about_new_message(sender, instance, created, *args, **kwargs):
    author = instance.author
    chat = instance.chat
    receivers = chat.members.exclude(id=author.id)

    message = f"User {author} sent a message in {chat}"
    for receiver in receivers:
        Notification.objects.create(user=receiver, text=message)
