from rest_framework import serializers
from .models import Outing

class OutingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outing
        fields = ['id', 'name', 'price']