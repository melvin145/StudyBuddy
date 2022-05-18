from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Room
from .serializers import Roomserializer

@api_view(["GET"])
def getroutes(request):
    routes=[
        "GET /api/rooms",
        "GET /api/rooms/:id"
    ]
    return Response(routes)

@api_view(["GET"])
def getrooms(request):
    room=Room.objects.all()
    serializer=Roomserializer(room,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getroom(request,pk):
    room=Room.objects.get(id=pk)
    serializer=Roomserializer(room,many=False)
    return Response(serializer.data)