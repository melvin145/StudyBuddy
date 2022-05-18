from django import views
from django.urls import path
from.views import getroom, getrooms, getroutes

urlpatterns=[
    path("",getroutes),
    path("rooms/",getrooms),
    path("rooms/<int:pk>/",getroom)
]