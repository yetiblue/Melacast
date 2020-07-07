
from rest_framework import viewsets
# from rest_framework.views import APIView
from .serializers import HeroSerializer, ActorSerializer,ListingsSerializer,UserappsSerializer
from .models import Hero,Actors,Listings, User_applications


from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action 
# from .serializers import PostSerializer



 



class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('alias')
    serializer_class = HeroSerializer

    def my_view(self,request):
        # queryset = Hero.objects.all().order_by('alias')
        queryset_serializer = HeroSerializer(queryset, context={"request": request})
        queryset_serializer.data






class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actors.objects.all().order_by('firstname')

    serializer_class = ActorSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        # qs = self.get_queryset
        if self.request.GET.get("firstname"):
            qs = qs.filter(firstname='Bob')
            return qs


    # def get(self,request,*args, **kwargs):
    #     queryset = Actors.objects.all()
    #     serializer = ActorSerializer(queryset, many=True, context={"request":request})
    #     return Response(serializer.data, status=status.HTTP_200_OK)




    # @action(detail=True, methods=["GET"])
    # def post(self,request, id=None):
class ListingsViewSet(viewsets.ModelViewSet):
    queryset = Listings.objects.all().order_by('location')
    serializer_class = ListingsSerializer

class UserappsViewSet(viewsets.ModelViewSet):
    queryset = User_applications.objects.all().order_by('status')
    serializer_class = UserappsSerializer
      
      