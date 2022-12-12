from django.shortcuts import render
from .serializers import *
from rest_framework import generics, permissions, status, viewsets
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
    
    city = request.GET.get('city')
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    if city:
        print('city sent')
        queryParam = f"location={city}"
    else:
        print('something else sent')
        queryParam = f"latitude={lat}&longitude={lng}"
    price = request.GET.get('price')
    term = f"term={request.GET.get('term')}"
    url = f"https://api.yelp.com/v3/businesses/search?{queryParam}&{term}&categories=&price={price}&sort_by=best_match&matches_party_size_param=true&limit=5"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer MirzBJCP0rFnEzwjGZKMhO8tiXa3oyOeJO7JpCIr7ExtZAmAmScyj4wjuMlrR28Msy97mfUV7GDnEXLNak8-gSn8ReYrVhTj9vrrgrgjM86SnIuXeCUytkvY1nOHY3Yx"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return HttpResponse(json.dumps(data), content_type="application/json")

class RetrieveActivityView(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        username = self.request.user
        return Activity.objects.filter(user=username)


class RetrieveUserActivityView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer

