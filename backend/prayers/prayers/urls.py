from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework_jwt.views import obtain_jwt_token


router = routers.DefaultRouter()
router.register('prayer_requests', views.PrayerRequestViewSet)
router.register('prayer_events', views.PrayerEventViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', obtain_jwt_token, name='token'),
]
