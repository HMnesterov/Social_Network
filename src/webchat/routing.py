from django.urls import re_path
from .consumers import ChatRoomConsumer
websocket_urlpatterns = [
    re_path(r'ws/chat/current_chat/(?P<room_id>\w+)/$', ChatRoomConsumer.as_asgi()),

]