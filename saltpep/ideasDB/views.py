from django.shortcuts import render
from .serializers import *
from rest_framework import generics, permissions, status
from .models import *
import requests
import json
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView

class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveOutingView(generics.ListAPIView):
    queryset = Outing.objects.all()
    serializer_class = OutingSerializer

def YelpView(request):
    price = request.GET.get('price')
    term = f"term={request.GET.get('term')}"
    url = f"https://api.yelp.com/v3/businesses/search?location=Lexington&{term}&categories=&price={price}&sort_by=best_match&matches_party_size_param=true&limit=3"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer MirzBJCP0rFnEzwjGZKMhO8tiXa3oyOeJO7JpCIr7ExtZAmAmScyj4wjuMlrR28Msy97mfUV7GDnEXLNak8-gSn8ReYrVhTj9vrrgrgjM86SnIuXeCUytkvY1nOHY3Yx"
    }
    # term = self.request.GET.get('term')
    print(term)
    print(price)
    response = requests.get(url, headers=headers)
    data = response.json()
    return HttpResponse(json.dumps(data), content_type="application/json")

class RetrieveActivityView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class RetrieveUserActivityView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer

