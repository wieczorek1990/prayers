from django.db import models


class PrayerRequest(models.Model):
    description = models.TextField()
    requester = models.TextField()


class PrayerEvent(models.Model):
    name = models.TextField()
    description = models.TextField()
    prayer_requests = models.ManyToManyField('PrayerRequest')
