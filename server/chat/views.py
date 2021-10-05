from re import S
from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request, 'index.html')

# def room (request, room_name):
#     return render (request, 'chatroom.html', {
#         'room': room_name
#     })


# Class Based Serializer Views
from .models import Room, Message
from .serializers import MessageSerializer, RoomSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

class RoomList (APIView):
    """
    List all rooms or create a new room
    """
    def get (self, request, format = None):
        """
        List all the rooms
        """
        rooms = Room.objects.all ()
        serializer = RoomSerializer (rooms, many = True)
        return Response (serializer.data)

    def post (self, request, format = None):
        """
        Create a new room
        """
        serializer = RoomSerializer (data = request.data)
        if serializer.is_valid ():

            # Check for duplciate room name
            # if the room name exists throw an error
            # create a new room
            if Room.objects.filter (room = request.data['room']).exists():
                return Response ({'Results': 'Duplicate Value'}, status = status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save ()
                return Response ({"New Room Created": 'Successful'}, status = status.HTTP_201_CREATED)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class RoomDetail (APIView):
    """
    Show room details
    """
    def get_object (self, pk):
        try:
            return Room.objects.get (pk = pk)
        except Room.DoesNotExist:
            return Http404

    def get (self, request, pk, format = None):
        try:
            room = Room.objects.get (id = pk)
            serializer = RoomSerializer (room, many = False)
            return Response (serializer.data)
        except:
            return Response ({"Response": "Invalid Room Number"}, status = status.HTTP_400_BAD_REQUEST)




@api_view (['GET'])
def messageList (request):
    """
    Get all the messages in the database irrespective of their room
    """
    try:
        if request.method == 'GET':
            messages = Message.objects.all ()
            serializer = MessageSerializer (messages, many = True)
            return Response (serializer.data)
    except:
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)  

@api_view (['POST'])
def messagePost (request, room_id):
    # Get the body of the data
    data = request.data
    # Append the room key in the data dictionary
    data['room'] = room_id
    # Serialize the data
    serializer = MessageSerializer (data = data)
    if serializer.is_valid():
        serializer.save()
        return Response ({"Reponse": "New Message Created"}, status = status.HTTP_201_CREATED)
    return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)  

@api_view (['GET'])
def messageDetail (request, room_id):
    """
    Get all the messages in a particular room
    """
    if request.method == 'GET':
        # Get the room with the id that's provided by the room_id variable
        # IF room exists execute the following if block 
        if Room.objects.filter (pk = room_id).exists ():
            messages = Message.objects.filter (room = room_id)
            serializer = MessageSerializer (messages, many = True)
            return Response (serializer.data)
        # if room_id is an invalid room number
        else:
            return Response ({"Response": "Invalid Room ID"}, status = status.HTTP_400_BAD_REQUEST)

