from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Baseball, Seat, Football
from .serializers import BlockSerializer,BaseballSerializer, SeatSerializer, FootballSerializer, RandomTLBaseballSerializer, RandomTLFootballSerializer
from django.db.models import Q
import random 

class BaseballInfo(APIView):
    def get(self, request):
        eng = self.request.query_params.get('eng')
        BB = Baseball.objects.get(eng=eng)
        if(BB != None):
            serializer = BaseballSerializer(BB)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)



class FootballInfo(APIView):
    def get(self, request):
        eng = self.request.query_params.get('eng')
        BB = Football.objects.get(eng=eng)
        if(BB != None):
            serializer = FootballSerializer(BB)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
class SeatInfo(APIView):
    def get(self, request):
        blockId = self.request.query_params.get('blockId')
        gradeId = self.request.query_params.get('gradeId')
        seats = Seat.objects.filter(Q(blockId=blockId) & Q(gradeId=gradeId))
        if(seats != None):
            serializer = SeatSerializer(seats, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

class selectGradeSignal(APIView):
    def get(self, request):
        gradeId = self.request.query_params.get('gradeId')
        return Response({"gradeId":gradeId})


class RandomTL(APIView):
    def get(self,request):
        random_num = random.randint(0,1)
        if(random_num==0):
            bs = Baseball.objects.all()
            random_bs = random.choice(bs)
            serializer = RandomTLBaseballSerializer(random_bs)
        else:
            fb = Football.objects.all()
            random_fb = random.choice(fb)
            serializer = RandomTLFootballSerializer(random_fb)
        return Response(serializer.data)