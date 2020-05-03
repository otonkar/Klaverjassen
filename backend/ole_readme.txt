https://channels.readthedocs.io/en/latest/tutorial/part_1.html

# create virtual env
python3 -m venv venv1
source venv1/bin/activate

python -m pip install --upgrade pip
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install django-computed-property	
pip install django-filter		
#pip install openpyxl	

pip install django-extensions
pip install django-cors-headers		

#---- Install for channel support
pip install channels
pip install channels_redis

--- Niet nodig
#pip install hiredis
#pip install -U asgiref
##pip install -U asgi_redis
#pip install redis      #?? needed?
#pip install channels_redis





# Reconnect websocket:  https://github.com/joewalnes/reconnecting-websocket

# Create Django project
django-admin startproject back1
cd back1
python manage.py startapp auth


# Start docker before starting django server
# Same port as in setting.py
docker run -p 6379:6379 -d redis:5

(   docker ps
    docker stop .....
    docker images)


# test that channels layers is working 
python manage.py shell
--- type in python shell ----
import channels.layers
channel_layer = channels.layers.get_channel_layer()
from asgiref.sync import async_to_sync
async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
async_to_sync(channel_layer.receive)('test_channel')
{'type': 'hello'}




# Async version
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))



