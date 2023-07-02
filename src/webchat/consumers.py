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
        text_data_in_json: dict = json.loads(text_data)
        message: str = text_data_in_json['message']
        username: str = text_data_in_json['username']
        chat_id: int = text_data_in_json['chat_id']
        r_type: str = text_data_in_json["type"]
        msg_id: int = text_data_in_json.get('msg_id', None)
        await self.channel_layer.group_send(
            self.room_group_name,
            {'message': message,
             'username': username,
             "chat_id": chat_id,
             "msg_id": msg_id,
             'type': r_type}
        )

    async def send_chat_message(self, event):
        message: str = event['message']
        username: str = event['username']
        chat_id: str = event["chat_id"]
        msg_id: int = await self.post_message(message=message, username=username, chat_id=chat_id)
        await self.send(text_data=json.dumps({'message': message, 'username': username, "msg_id": msg_id}))

    async def delete_chat_message(self, event):
        msg_id: int = event["msg_id"]
        username: str = event['username']
        if not msg_id:
            await self.send(text_data=json.dumps({"success": False}))
        else:
            await self.remove_message(message_id=msg_id, username=username)
            await self.send(text_data=json.dumps({"success": True}))

    async def edit_chat_message(self, event):
        msg_id: int = event["msg_id"]
        username: str = event['username']
        if msg_id:
            await self.edit_message(message_id=msg_id, username=username)
            await self.send(text_data=json.dumps({"success": True}))
        else:
            await self.send(text_data=json.dumps({"success": False}))

    @database_sync_to_async
    def post_message(self, message, username, chat_id) -> int:
        guy = get_object_or_404(Person, username=username)
        chat = get_object_or_404(Chat, id=chat_id)
        return Message.objects.create(text=message, author=guy, chat=chat).id

    @database_sync_to_async
    def remove_message(self, message_id: int, username: str) -> bool:
        guy: Person = get_object_or_404(Person, username=username)
        msg: Message = get_object_or_404(Message, id=message_id)
        if msg.author == guy or msg.chat.admin == guy:
            msg.delete()
            return True
        return False

    @database_sync_to_async
    def edit_message(self, message_id: int, username: str, new_text: str) -> bool:
        guy: Person = get_object_or_404(Person, username=username)
        msg: Message = get_object_or_404(Message, id=message_id)
        if msg.author == guy and new_text:
            msg.text = new_text
            msg.save()
            return True

        return False
