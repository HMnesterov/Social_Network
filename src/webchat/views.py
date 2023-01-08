from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from user.models import Person
from webchat.forms import CreateChatForm
from webchat.models import Chat


@login_required
def room(request, room_id):
    chat = get_object_or_404(Chat, id=room_id)
    chat_members = chat.members.all()
    if request.user not in chat_members:
        return redirect('user_profile', id=request.user.id)
    non_in_chat = request.user.friends.exclude(id__in=[i.id for i in chat_members])
    old_messages = chat.chat_messages.all()
    return render(request, 'chat/chatroom.html',
                  {'room_name': chat.title,
                   'old_messages': old_messages,
                   'room_id': chat.id, 'new_persons': non_in_chat})



@login_required
def all_chats(request):
    chats = request.user.chats.all()
    return render(request, 'chat/all_chats.html', {'chats': chats})

@login_required
def create_new_chat(request):
    form = CreateChatForm()

    if request.method == "POST":
        form = CreateChatForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.admin = request.user
            form.save()
            form.instance.members.add(request.user)
            form.save()
            return redirect('chats')
    return render(request, 'chat/create_chat.html', {'form': form})



@login_required
def add_new_user_to_chat(request, chat_id, user_id):

    user = get_object_or_404(Person, id=user_id)
    chat = get_object_or_404(Chat, id=chat_id)
    chat.members.add(user)
    chat.save()
    return JsonResponse({'thanks': "a lot"})

