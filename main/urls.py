from urllib.parse import urlparse
from django.urls import path
from.views import *

urlpatterns=[
    path("",home,name="home"),
    path("create-room",CreateRoom,name="createroom"),
    path("room/<int:pk>/",Rooms,name="room"),
    path("update-room/<int:pk>/",UpdateRoom,name="updateroom"),
    path("delete-room/<int:pk>/",DeleteRoom,name="deleteroom"),
    path("login",Loginview,name="login"),
    path("register",Registration,name="register"),
    path("logout",Logoutview,name="logout"),
    path("topics",Topicview,name="topics"),
    path("activity",Activity,name="activity"),
    path("user",UserView,name="user"),
]