
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    extra_kwargs = {'password': {'write_only': True}}
    # activity = models.OneToManyField('Activity', through="UserActivity")

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        
    def __str__(self):
        return self.username

class Outing(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Activity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    picture_url = models.URLField(max_length=300)
    rating = models.FloatField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    address = models.CharField(max_length=75)
    created_at = models.DateField(auto_now=True)
    scheduled_for = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    completed_on = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)


class UserActivity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, blank=True, null=True)
    





