from django.urls import path
from .views import room, all_chats, create_new_chat, add_new_user_to_chat

urlpatterns = [
    path('create_chat', create_new_chat, name='create_chat'),
    path('all_chats', all_chats, name='chats'),
    path('current_chat/<int:room_id>/', room, name='chat-room'),
    path('current_chat/add_user/<int:chat_id>/<int:user_id>/', add_new_user_to_chat, name='add-to-chat')


]