from django.shortcuts import render
from .serializers import OutingSerializer
from rest_framework import generics
from .models import Outing
import requests
import json
from django.http import HttpResponse


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


