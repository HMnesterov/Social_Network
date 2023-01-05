from django.urls import path
from .views import enter_room

urlpatterns = [
    path('', enter_room, name='enter_room'),
    path('<str:room_name>/', room, name='chat-room'),

]