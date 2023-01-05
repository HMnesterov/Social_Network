from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
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
        print(f"сообщение {message} от {username}")

        await self.channel_layer.group_send(
            self.room_group_name,
            {'message': message,
             'username': username,
             'type': 'chat_message'}
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({'message': message, 'username': username,}))