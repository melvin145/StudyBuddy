from pyexpat import model
from rest_framework.serializers import ModelSerializer
from main.models import Room

class Roomserializer(ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'