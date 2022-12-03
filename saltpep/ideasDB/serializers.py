from rest_framework import serializers
from .models import Outing, CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class CustomUserSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
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