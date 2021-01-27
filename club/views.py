from django.shortcuts import render
from .models import Meeting, MeetingMinute, Resource, Event 

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def meeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meeting.html', {'meeting_list': meeting_list})

def meetingminute(request):
    meetingminute_list=MeetingMinute.objects.all()
    return render(request, 'club/meetingminute.html', {'meetingminute_list': meetingminute_list})

def resource(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resource.html', {'resource_list': resource_list})

def event(request):
    event_list=Event.objects.all()
    return render(request, 'club/event.html', {'event_list': event_list})    