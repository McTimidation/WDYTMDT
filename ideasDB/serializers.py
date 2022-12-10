from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .fields import *



class CustomUserSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    # activities = UserActivityListingField(many=True, queryset=UserActivity.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        

class OutingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outing
        fields = ['id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserListingField(queryset=CustomUser.objects.all())
    class Meta:
        model = Activity
        fields = ['user', 'name', 'phone', 'picture_url', 'rating', 'city', 'state', 'address', 'created_at', 'scheduled_for', 'completed_on']

class UserActivitySerializer(serializers.ModelSerializer):
    user = UserListingField(queryset=CustomUser.objects.all())
    activity = ActivityListingField(queryset=Activity.objects.all())
    class Meta:
        model = UserActivity
        fields = ['user', 'activity']