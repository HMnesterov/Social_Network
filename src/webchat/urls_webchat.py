from django.urls import path
from .views import room, all_chats, add_new_user_to_chat, leave_from_chat

urlpatterns = [
    path('all_chats', all_chats, name='chats'),
    path('current_chat/<int:room_id>/', room, name='chat-room'),
    path('current_chat/add_user/<int:chat_id>/<int:user_id>/', add_new_user_to_chat, name='add-to-chat'),
    path('current_chat/delete_user/<int:chat_id>/<int:user_id>/', leave_from_chat, name='kick-from-chat'),


]