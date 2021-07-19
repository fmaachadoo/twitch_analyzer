from django.shortcuts import render
from rest_framework import viewsets, serializers

from src.models import Game

class GameSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)


class GameView(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

    def get_queryset(self):
        return super().get_queryset()
    