from __future__ import unicode_literals

import datetime
import json
import pytz

from django.http import Http404
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from schedule.models import Calendar, CalendarRelation, Event
from schedule.serializer import EventSerializer
from schedule.models.calendars import Calendar
from schedule.models.events import Event

from doctor.models import Doctors
from subtitle.models import Subtitles

class TestViewAPI(TestCase):
    def setUp(self):
        doctor = Doctors(name = 'Victor', registration= '112020122',CPF='1637615253',status =True, category='1231233212')
        doctor.save()
        calendar = Calendar(name = 'Test Calendar')
        calendar.save()
        subtitle = Subtitles(1)
        self.event_attr = {
            'id':1,
            'subtitle': subtitle,
            'start': datetime.datetime(2013, 1, 5, 8, 0, tzinfo=pytz.utc),
            'end': datetime.datetime(2013, 1, 5, 9, 0, tzinfo=pytz.utc),
            'doctor': doctor,
            'calendar': calendar
        }

        self.serializer_data = {
            'id':0,
            'subtitle':subtitle,
            'start': datetime.datetime(2013, 1, 5, 8, 0, tzinfo=pytz.utc),
            'end': datetime.datetime(2013, 1, 5, 9, 0, tzinfo=pytz.utc),
            'doctor':doctor,
            'calendar': calendar
        }
        self.event = Event.objects.create(**self.event_attr)
        self.serializer = EventSerializer(instance=self.event)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(['subtitle', 'doctor', 'id', 'end_recurring_period', 'hospital', 'updated_on', 'end', 'calendar', 'creator', 'description', 'created_on', 'start']),set(data.keys()))

    def test_field_response_subtitle(self):
        self.assertEqual(self.serializer_data['subtitle'],self.event_attr['subtitle'])

    def test_field_response_start(self):
       self.assertEqual(self.serializer_data['start'],self.event_attr['start'])

    def test_field_response_end(self):
       self.assertEqual(self.serializer_data['end'],self.event_attr['end'])

    def test_field_response_doctor(self):
       self.assertEqual(self.serializer_data['doctor'],self.event_attr['doctor'])

    def test_field_response_calendar(self):
       self.assertEqual(self.serializer_data['calendar'],self.event_attr['calendar'])
