from django.urls import path
from .views import enter_room, room

urlpatterns = [
    path('<str:room_name>/', room, name='chat-room'),

]