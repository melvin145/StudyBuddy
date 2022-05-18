from operator import le
from pydoc_data.topics import topics
from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q,Count
from django.contrib.auth import authenticate,login,logout
from .forms import RoomcreationForm,RegistrationForm
from django.contrib import messages

# Create your views here.
def home(request):
    q=request.GET.get("q") if request.GET.get("q")!=None else ""
    topics=Topic.objects.filter(name__icontains=q)
    topic_count=len(topics)
    rooms=Room.objects.annotate(noOfparticipnts=Count("participants")).filter(
            Q(topic__name__icontains=q)|
            Q(host__username__icontains=q)|
            Q(title__icontains=q)|
            Q(description__icontains=q)
        ).order_by("-noOfparticipnts")
    messages=Messages.objects.all()[0:5]
    return render(request,"index.html",{"rooms":rooms,"messages":messages,"topics":topics,"topic_count":topic_count})


#ROOM VIEW
def Rooms(request,pk):
    room=Room.objects.get(id=pk)
    message=room.messages_set.all()
    participant=room.participants.all()
    if request.method=="POST":
        Messages.objects.create(content=request.POST.get("message"),room=room,user=request.user)
        room.participants.add(request.user)
        return redirect(Rooms,room.id)
    
    return render(request,"room.html",{"message":message,"room":room,"participants":participant})

#Create a New Room
def CreateRoom(request):
    form=RoomcreationForm()
    if request.method=='POST':
        form=RoomcreationForm(request.POST)
        if form.is_valid():
            topic=form.cleaned_data["topic"]
            title=form.cleaned_data["title"]
            description=form.cleaned_data["description"]
            room=Room.objects.create(host=request.user,topic=topic,title=title,description=description)
            return redirect(Rooms,room.id)
        else:
            return redirect(home)
    else:
        form=RoomcreationForm()          
        return render(request,"create-room.html",{"form":form})

# View to update the selected room 
def UpdateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomcreationForm(instance=room)
    if request.method=='POST':
        form=RoomcreationForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            return redirect(home)
                 
    return render(request,"update-room.html",{"form":form})

#View to delete the selected room
def DeleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    room.delete()
    return redirect(home)

    
# view to login the user      
def Loginview(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        try:
            user=authenticate(username=username,password=password)
        except:
              messages.error(request,"Enter the Name and password correctly")
              return redirect(Loginview)

        if user!=None:
            login(request,user)
            return redirect(home)
    return render(request,"login.html")

# Register the user
def Registration(request):
    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Loginview)
        else:
            messages.error(request,"check email and password (password should contain atleat 8 characters with numbers,symbols eg: Helooworld345#")
    return render(request,"register.html",{"form":form})
 
#logout View
def Logoutview(request):
    user=request.user
    logout(request)
    return redirect(Loginview)

def Topicview(request):
    q=request.GET.get("q") if request.GET.get("q")!=None else ""
    topic=Topic.objects.filter(name__icontains=q)
    return render(request,"topics.html",{"topic":topic})

def Activity(request):
    user=request.user
    message=Messages.objects.filter(user=user)[0:5]
    return render(request,"activity.html",{"message":message})

def UserView(request):
    user=User.objects.get(username=request.user)
    return render(request,"profile.html",{"user":user})