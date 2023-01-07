from django.urls import path
from .views import room, all_chats, create_new_chat

urlpatterns = [
    path('create_chat', create_new_chat, name='create_chat'),
    path('all_chats', all_chats, name='chats'),
    path('current_chat/<str:room_id>/', room, name='chat-room'),


]