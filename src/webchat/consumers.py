import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import get_object_or_404

from user.models import Person
from webchat.models import Chat, Message


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_id']

        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_in_json = json.loads(text_data)
        message = text_data_in_json['message']
        username = text_data_in_json['username']
        chat_id = text_data_in_json['chat_id']


        await self.post_message(message=message, username=username, chat_id=chat_id)
        await self.channel_layer.group_send(
            self.room_group_name,
            {'message': message,
             'username': username,
             'type': 'chat_message'}
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({'message': message, 'username': username, }))


    @database_sync_to_async
    def post_message(self, message, username, chat_id):
        guy = get_object_or_404(Person, username=username)
        chat = get_object_or_404(Chat, id=chat_id)
        Message.objects.create(text=message, author=guy, chat=chat)
        print(f"сообщение {message} от {guy} в {chat_id}")
