from django.urls import path
from .views import BaseballInfo,SeatInfo,selectGradeSignal, FootballInfo, RandomTL

urlpatterns = [
    path('api/football/info/', FootballInfo.as_view(), name='footballinfo'),
    path('api/baseball/info/', BaseballInfo.as_view(), name='baseballinfo'),
    path('api/seat/', SeatInfo.as_view(), name='seats'),
    path('api/sgs/', selectGradeSignal.as_view(), name='sgs'),
    path('api/randomtl/',RandomTL.as_view(), name='randomtl'),
]