from django.urls import path
from .views import  room

urlpatterns = [
    path('<str:room_name>/', room, name='chat-room'),

]