from django.shortcuts import render
from rest_framework import generics
from .models import Players
from .serializers import AverageScoreSerializer,PlayerNameSerializer
from django.db.models import Avg
from rest_framework.response import Response



# Create your views here.
class AverageScore(generics.ListAPIView):
    queryset=(Players.objects.values('Nationality').annotate(Overall=Avg('Overall')).order_by())
    serializer_class=AverageScoreSerializer

class PlayerName(generics.ListAPIView):
    queryset=Players.objects.all()
    def get(self,request,score=None):
        data=Players.objects.filter(Overall__gte=score)
        serializer_class=PlayerNameSerializer(data,many=True)
        return Response(serializer_class.data)


