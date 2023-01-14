from django.shortcuts import render
from django.views import View


def view(request):
    return render(request, 'videochat/chatroom.html')
