from rest_framework import test, status
from django.shortcuts import reverse
from django.contrib.auth.models import User

from api import models


class BasicApiTestCase(test.APITestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'abcd1234'

        self.requester = 'Łukasz'
        self.decription = 'Silence my ears o Lord.'

        self.event_name = 'Holy Mass Sołacz 19:00'
        self.event_description = 'ul. Podlaska 10'

    def test_happy_scenario(self):
        # User creation
        user = User.objects.create_user(self.username,
                                        password=self.password)
        response = self.client.post(reverse('token'), data={
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Creating prayer request
        self.client.force_authenticate(user=user)
        response = self.client.post(reverse('prayerrequest-list'), data={
            'requester': self.requester,
            'description': self.decription,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        prayer_request = models.PrayerRequest.objects.get(id=response.json()['id'])

        # Creating prayer event
        response = self.client.post(reverse('prayerevent-list'), data={
            'name': self.event_name,
            'description': self.event_description,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        prayer_event = models.PrayerEvent.objects.get(id=response.json()['id'])

        # Adding prayer request to prayer event
        # TODO(lwieczorek): implement
