from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from webchat.models import Chat

DOMAIN = '127.0.0.1:8000'





@login_required
def room(request, room_name):
    chat = Chat.objects.get_or_create(title=room_name)[0]

    old_messages = chat.chat_messages.all()
    if not old_messages:
        old_messages = None
    chat.members.add(request.user)


    return render(request, 'chat/chatroom.html', {'room_name': room_name, 'old_messages': old_messages})