from rest_framework import viewsets

from api import models, serializers


class PrayerRequestViewSet(viewsets.ModelViewSet):
    queryset = models.PrayerRequest.objects.all()
    serializer_class = serializers.PrayerRequestSerializer


class PrayerEventViewSet(viewsets.ModelViewSet):
    queryset = models.PrayerEvent.objects.all()
    serializer_class = serializers.PrayerEventSerializer


class PrayerViewSet(viewsets.ModelViewSet):
    queryset = models.Prayer.objects.all()
    serializer_class = serializers.PrayerSerializer
