from rest_framework import serializers
from .models import *

class UserListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.username

    def to_internal_value(self, data):
        return CustomUser.objects.get(id=data)


class OutingListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.title

    def to_internal_value(self, data):
        return Outing.objects.get(name=data)


class ActivityListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.title

    def to_internal_value(self, data):
        return Activity.objects.get(name=data)
        

class UserActivityListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.title

    def to_internal_value(self, data):
        return UserActivity.objects.get(name=data)

