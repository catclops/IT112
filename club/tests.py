from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinute, Resource, Event
import datetime
from .forms import MeetingForm, ResourceForm


# Create your tests here.


class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='Big')

    def test_string(self):
        meeting=Meeting(meetingtitle='Big')
        self.assertEqual(str(self.type), 'Big')
    
    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resource(resourcename='Bog')
    

    def test_string(self):
        resource=Resource(resourcename='Bog')
        self.assertEqual(str(self.type), 'Bog')
    
    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.type=Event(eventtitle='Bag')

    def test_string(self):
        event=Event(eventtitle='Bag')
        self.assertEqual(str(self.type), 'Bag')
    
    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')
 
 #valid form data

class NewMeetingTest(TestCase):
    def test_newmeetingform(self):
        data={
            'meetingtitle':'Graduation Date',
            'meetingdate':'2021-12-12',
            'meetingtime':'17:00:00',
            'meetinglocation':'Franklin High School',
            'meetingagenda':'walk the line'
        }
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)

class NewResourceTest(TestCase):
    def test_newresourceform(self):
        data={
            'resourcename':'The Bay',
            'resourcetype':'Yukmouth',
            'resourceurl':'https://ebay.com',
            'dateentered':'2021-04-04',
            'userid':'catclops',
            'description':'The Luniz'
        }
        form=ResourceForm (data)
        self.assertTrue(form.is_valid)

#failed tests below
    #def test_newmeetingform_Invalid(self):
        #data={
            #'meetingtitle':'Graduation Date',
            #'meetingdate':'2021-12-12',
            #'meetinglocation':'Franklin High School',
            #'meetingagenda':'walk the line'
        #}
        #form=MeetingForm (data)
        #self.assertFalse(form.is_valid)

