from django.urls import path

from .views import CardInfo

urlpatterns = [
    path('api/info/', CardInfo.as_view(), name='cardinfo'),
]