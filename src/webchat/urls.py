from django.urls import path
from .views import chatroom_page, all_chats_where_current_user_participate_in, add_new_user_to_chat, leave_from_current_chat

urlpatterns = [
    path('all_chats', all_chats_where_current_user_participate_in, name='chats'),
    path('current_chat/<int:room_id>/', chatroom_page, name='chat-room'),
    path('current_chat/add_user/<int:chat_id>/<int:user_id>/', add_new_user_to_chat, name='add-to-chat'),
    path('current_chat/delete_user/<int:chat_id>/<int:user_id>/', leave_from_current_chat, name='kick-from-chat'),


]