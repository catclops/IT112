from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meeting/', views.meeting, name='meeting'),
    path('meetingminute/', views.meetingminute, name='meetingminute'),
    path('resource/', views.resource, name='resource'),
    path('event/', views.event, name='event'),
]