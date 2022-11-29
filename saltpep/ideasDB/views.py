from django.shortcuts import render
from .serializers import OutingSerializer
from rest_framework import generics
from .models import Outing

class RetrieveOutingView(generics.ListAPIView):
    queryset = Outing.objects.all()
    serializer_class = OutingSerializer




