from django.forms import widgets
from rest_framework import serializers
from main_app.models import Hotels, Cities, Owners, Reviews

class HotelsSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(many=True, queryset=Reviews.objects.all())
    class Meta:
        model = Hotels
        fields = ('url', 'name', 'description', 'facilities', 'location', 'city', 'price', 'owner', 'reviews')
        
class Hotels1Serializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.SlugRelatedField(many=True, queryset=Reviews.objects.all(), slug_field='text')

    class Meta:
        model = Hotels
        fields = ('url', 'name', 'description', 'facilities', 'location', 'city', 'price', 'owner', 'reviews')
        
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
        
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('text', 'hotel', 'author', 'grade', 'date')