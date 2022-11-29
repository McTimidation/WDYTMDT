from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
# router.register(r'outings', RetrieveOutingView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('outings/', RetrieveOutingView.as_view())
]