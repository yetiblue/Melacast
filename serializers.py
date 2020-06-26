from rest_framework import serializers


from .models import Hero, Timmy,Actors

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields=('name', 'alias')

class TimmySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timmy
        fields=('name', 'date')
class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actors
        fields=('firstname', 'lastname','experience','headshot')



      