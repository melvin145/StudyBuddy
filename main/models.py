from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
       return self.name

class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    participants=models.ManyToManyField(User,related_name='participants')
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Messages(models.Model):
    content=models.TextField(null=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE ,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=["-created_at"]
