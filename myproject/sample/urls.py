from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import URLViewSet, home

router = DefaultRouter()
router.register(r'urls', URLViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
]
