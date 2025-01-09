import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message  # Import models directly, no circular imports here

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Handle disconnection
        pass

    async def receive(self, text_data):
        try:
            # Safely parse the incoming JSON message
            text_data_json = json.loads(text_data)
            message = text_data_json.get('message')
            user = self.scope.get('user')

            if user and user.is_authenticated:
                # Save message to the database and send it back to the client
                await self.send(text_data=json.dumps({'message': message}))
                await self.save_message(user, message)  # Calling the async method for DB interaction
            else:
                # Notify the client that authentication is required
                await self.send(text_data=json.dumps({'error': 'Login required'}))

        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({'error': 'Invalid message format'}))

    async def save_message(self, user, content):
        """Separate async method for saving messages to avoid blocking."""
        await Message.objects.acreate(user=user, content=content)  # `acreate` for async DB interaction
