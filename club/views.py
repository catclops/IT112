from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinute, Resource, Event
from django.urls import reverse_lazy
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required

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

# Assignment 6 Here
def meetingdetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetail.html', {'meeting': meeting})  

def resourcedetail(request, id):
    resource=get_object_or_404(Resource, pk=id)
    return render(request, 'club/resourcedetail.html', {'resource': resource})      

#Assignment 8 forms below
@login_required
def newmeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})
    
@login_required
def newresource(request):
    form=ResourceForm

    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm
    else:
        form=ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')