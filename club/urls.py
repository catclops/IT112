from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meeting/', views.meeting, name='meeting'),
    path('meetingminute/', views.meetingminute, name='meetingminute'),
    path('resource/', views.resource, name='resource'),
    path('event/', views.event, name='event'),
    #Assignment 6 Below
    path('meetingdetail/<int:id>', views.meetingdetail, name='meetingdetail'),
    path('resourcedetail/<int:id>', views.resourcedetail, name='resourcedetail'),
    #Assignment 8 forms below
    path('newmeeting/', views.newmeeting, name='newmeeting'),
    path('newresource/', views.newresource, name='newresource'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]