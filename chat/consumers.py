import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels_presence.models import Room
from channels_presence.models import Presence
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
import asyncio



class ChatConsumer(AsyncWebsocketConsumer):
    room = {} 
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user_name = self.scope['url_route']['kwargs']['user_name']
        

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        
        await self.accept()
  

        
    async def disconnect(self, close_code):


        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        ) 




    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')
        user = text_data_json.get('user')
        action = text_data_json.get('action')
        
        
        
        # User disconnect
        if action == 'disconnect':
            data = {
                'type': 'chat_message',
                'message': f'{message}'
            }


        # User connect
        if action == 'connect':
            data = {
                'type': 'chat_message',
                'message': f'{message}',            
            }

            


        # Data to message
        if action == 'message':
            data = {
                'type': 'chat_message',
                'message': f'{user}: {message}',              
            }     
            

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,data
        )
   
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
    
        

        # Send message to WebSocket
        await self.send(
            text_data = json.dumps({
            'message': message,
            'room': '',
            # self.room_name: self.online,
        }))
            
        
