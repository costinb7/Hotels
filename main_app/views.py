from django.shortcuts import render
from main_app.models import Hotels, Cities, Owners
from rest_framework import viewsets
from main_app.serializers import HotelsSerializer, CitiesSerializer, OwnersSerializer
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'hotels': reverse('hotels-list', request=request, format=format)
    })

# Create your views here.
class HotelsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer
    
class CitiesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    
class OwnersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Owners.objects.all()
    serializer_class = OwnersSerializer
    

    
class HotelsList(generics.ListAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer


class HotelsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer