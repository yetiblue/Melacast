
from rest_framework import viewsets

from .serializers import HeroSerializer, TimmySerializer, ActorSerializer
from .models import Hero,Timmy,Actors


from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action 
# from .serializers import PostSerializer



 



class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('alias')
    serializer_class = HeroSerializer

class TimmyViewSet(viewsets.ModelViewSet):
    queryset = Timmy.objects.all().order_by('name')
    serializer_class = TimmySerializer
class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actors.objects.all().order_by('firstname')
    serializer_class = ActorSerializer



    # @action(detail=True, methods=["GET"])
    # def post(self,request, id=None):
         