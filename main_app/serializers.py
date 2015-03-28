from django.forms import widgets
from rest_framework import serializers
from main_app.models import Hotels, Cities, Owners

class HotelsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotels
        fields = ('url', 'name', 'description', 'facilities', 'location', 'city', 'price', 'owner')
        
class CitiesSerializer(serializers.ModelSerializer):
    hotels = serializers.PrimaryKeyRelatedField(many=True, queryset=Hotels.objects.all())
    class Meta:
        model = Cities
        fields = ('name', 'zone',  'hotels')
        
class OwnersSerializer(serializers.ModelSerializer):
    hotels = serializers.SlugRelatedField(many=True, queryset=Hotels.objects.all(), slug_field='name')
    class Meta:
        model = Owners
        fields = ('name', 'phone', 'email', 'hotels')