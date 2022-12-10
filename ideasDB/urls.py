from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import *
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'activities', RetrieveActivityView, basename='activities')

urlpatterns = [
    path('', include(router.urls)),
    path('outings/', RetrieveOutingView.as_view()),

    path('yelpView/', YelpView),

    # path('Activities/', RetrieveActivityView.as_view()),

    path('UserActivity/', RetrieveUserActivityView.as_view()),
    path('UserActivity/<int:pk>/', RetrieveUserActivityView.as_view()),

    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)