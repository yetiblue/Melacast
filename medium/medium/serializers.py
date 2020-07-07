from rest_framework import serializers


from .models import Hero, Actors,Listings,User_applications

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model = Hero
        fields=('name', 'alias','photo','photo_url')

    def get_photo_url(self, queryset):
        request = self.context.get('request')
        photo_url = queryset.photo.url
        return request.build_absolute_uri(photo_url)

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actors
        fields=('firstname','middle', 'lastname','age','headshot','role','experience','ethnicity','bio','height_feet','height_inches','location')

class ListingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listings
        fields=('date','start_date','end_date','location','overview','studio','genre','status','job_type')

class UserappsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_applications
        fields=('role','company','status')


      