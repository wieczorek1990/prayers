from django.db import models
from django_extensions.db import models as db_models
from django.contrib.auth.models import User


class PrayerRequest(db_models.TimeStampedModel):
    requester = models.TextField()
    description = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Prayer(db_models.TimeStampedModel):
    prayer_request = models.OneToOneField('PrayerRequest',
                                          on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class PrayerEvent(db_models.TimeStampedModel):
    name = models.TextField()
    description = models.TextField()

    prayer_requests = models.ManyToManyField('PrayerRequest')

    def __str__(self):
        return str(self.id)
