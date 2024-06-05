from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from testsapp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'testlist', TestListViewSet)
router.register(r'users', UserIdentViewSet, basename='UserIdentViewSet'),

urlpatterns = [
    path('', include(router.urls)),
    path("index/", index, name='index'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user-profile/', UserProfileView.as_view(), name='user_profile'),

    path('gettest/', RandomTestAPIView.as_view(), name='random-test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)