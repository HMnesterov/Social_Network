from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from user.models import Person
from webchat.forms import CreateChatForm
from webchat.models import Chat


@login_required
def chatroom_page(request, room_id):
    chat = get_object_or_404(Chat, id=room_id)
    chat_members = chat.members.all()
    if request.user not in chat_members:
        return redirect('user_profile', id=request.user.id)
    non_in_chat = request.user.friends.exclude(id__in=[i.id for i in chat_members])
    old_messages = chat.chat_messages.all()
    return render(request, 'chat/chatroom.html',
                  {'room_name': chat.title,
                   'old_messages': old_messages,
                   'room_id': chat.id, 'new_persons': non_in_chat, 'chat_members': chat_members, 'admin': chat.admin})


@login_required
def all_chats_where_current_user_participate_in(request):
    form: CreateChatForm = CreateChatForm()
    if request.method == "POST":
        form = CreateChatForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.admin = request.user
            form.save()
            form.instance.members.add(request.user)
            form.save()
            return redirect('chats')
    chats = request.user.chats.all()
    return render(request, 'chat/all_chats.html', {'chats': chats, 'form': form})


@login_required
def add_new_user_to_chat(request, chat_id, user_id):
    user = get_object_or_404(Person, id=user_id)
    chat = get_object_or_404(Chat, id=chat_id)
    if not (request.user in chat.members.all()):
        return redirect('chats')
    chat.members.add(user)
    chat.save()
    return JsonResponse({'thanks': "a lot"})


@login_required
def leave_from_current_chat(request, chat_id, user_id):

    user = get_object_or_404(Person, id=user_id)
    chat = get_object_or_404(Chat, id=chat_id)
    if not (request.user == user or chat.admin == request.user):
        return redirect('chats')
    chat.members.remove(user)
    chat.save()
    return JsonResponse({'thanks': "a lot"})
