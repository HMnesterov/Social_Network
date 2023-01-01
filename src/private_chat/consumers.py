from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatWebSocket(AsyncWebsocketConsumer):
    async def connect(self):
        user_id = self.scope["session"]["_auth_user_id"]
        self.group_name = f"{user_id}"
        # connect to room

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        # Leave from room
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_in_json = json.loads(text_data)
        message = text_data_in_json['message']
        # send message to room group
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'receive_group_message',
                'message': message
            }
        )

    async def receive_group_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))

