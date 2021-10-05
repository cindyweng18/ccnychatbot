from django.urls import re_path
from . import consumers

# Call this the websocket_urlpatterns because it will be easier to understand whether it's a normal HTTP path or websocket path
websocket_urlpatterns = [
    re_path (r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer)
]