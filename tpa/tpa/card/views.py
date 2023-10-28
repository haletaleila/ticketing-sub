from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Card
from .serializers import CardSerializer

class CardInfo(APIView):
    def get(self, request):
        root_cards = Card.objects.filter(parent__isnull=True)
        
        if root_cards.exists():
            serializer = CardSerializer(root_cards, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
