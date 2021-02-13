from django.test import TestCase
from .models import Meeting, MeetingMinute, Resource, Event

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