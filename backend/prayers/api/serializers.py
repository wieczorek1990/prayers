from rest_framework import serializers

from api import models


class UserModelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )


class PrayerRequestSerializer(UserModelSerializer):
    class Meta:
        model = models.PrayerRequest
        fields = ('id', 'requester', 'description', 'user',)
        read_only_fields = ('id',)


class PrayerSerializer(UserModelSerializer):
    class Meta:
        model = models.Prayer
        fields = ('id', 'prayer_request', 'user',)
        read_only_fields = ('id',)


class PrayerEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrayerEvent
        fields = ('id', 'name', 'description')
        read_only_fields = ('id',)
