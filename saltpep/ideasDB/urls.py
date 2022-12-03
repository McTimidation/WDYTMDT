from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import *
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
# router.register(r'outings', RetrieveOutingView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('outings/', RetrieveOutingView.as_view()),
    path('yelpView/', YelpView),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('yelpView/<term>/<price>/', YelpView),
    # path('yelpView/<term>/', YelpView)
]