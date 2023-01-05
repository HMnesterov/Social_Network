from django.shortcuts import render, redirect

DOMAIN = '127.0.0.1:8000'


def enter_room(request):
    return render(request, 'enter_room.html', {'DOMAIN': DOMAIN})



def room(request, room_name):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'chatroom.html', {'room_name': room_name, 'old_messages': '\nniggers: hello'})