from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import *
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
# router.register(r'outings', RetrieveOutingView)

urlpatterns = [
    # path('', include(router.urls)),
    # path('outings/', RetrieveOutingView.as_view()),
    # path('yelpView/', YelpView),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]