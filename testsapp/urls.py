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




# Using the URLconf defined in kopa.urls, Django tried these URL patterns, in this order:
#
# api-auth/
# admin/
# ^testlist/$ [name='test-list']
# ^testlist\.(?P<format>[a-z0-9]+)/?$ [name='test-list']
# ^testlist/(?P<pk>[^/.]+)/$ [name='test-detail']
# ^testlist/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='test-detail']
# ^users/$ [name='UserIdentViewSet-list']
# ^users\.(?P<format>[a-z0-9]+)/?$ [name='UserIdentViewSet-list']
# ^users/(?P<pk>[^/.]+)/$ [name='UserIdentViewSet-detail']
# ^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='UserIdentViewSet-detail']
# [name='api-root']
# <drf_format_suffix:format> [name='api-root']
# index/ [name='index']
# api/token/ [name='token_obtain_pair']
# api/token/refresh/ [name='token_refresh']
# api/user-profile/ [name='user_profile']
# gettest/ [name='random-test']
# ^media/(?P<path>.*)$
# The current path, index/asd, didn’t match any of these.