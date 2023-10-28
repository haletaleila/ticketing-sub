from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()  # 재귀적으로 자식들을 가져옵니다.

    class Meta:
        model = Card
        fields = '__all__'

    def get_children(self, obj):
        # obj.children.all()를 사용하여 관련된 모든 자식 카드 객체를 가져옵니다.
        # 그리고 각 자식 카드 객체에 대해 CardSerializer를 사용하여 직렬화합니다.
        return CardSerializer(obj.children.all(), many=True).data