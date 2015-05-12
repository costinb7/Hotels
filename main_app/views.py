from django.shortcuts import render
from main_app.models import Hotels, Cities, Owners, Reviews
from rest_framework import viewsets
from main_app.serializers import HotelsSerializer, CitiesSerializer, OwnersSerializer, Hotels1Serializer, ReviewsSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from rest_framework.response import Response

form_city = None
form_name = None

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'hotels': reverse('hotels-list', request=request, format=format)
    })

# Create your views here.
class HotelsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class SearchHotelsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = Hotels1Serializer
    
    def list(self, request):
        print "in list"
        print form_name, "form_name"
        hotels = Hotels.objects.all()
        
        if form_name is not None:
            hotels = hotels.filter(name__startswith=form_name)
        if form_city is not None:
            hotels = hotels.filter(city__name=form_city)
        serializer = Hotels1Serializer(hotels, context={'request': request}, many=True)
        return Response(serializer.data)
    
    
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
    
class HotelForm(forms.Form):
    name = forms.CharField(required=False)
    city = forms.ModelChoiceField(queryset=Cities.objects.all(), required=False)
    price = forms.CharField(required=False)
    #class Meta:
    #    model = Hotels
    #    fields = ('name', 'city', 'price')
        
def post_form_upload(request):
    global form_city, form_name
    print "global form_City", form_city
    if request.method == 'GET':
        form = HotelForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = HotelForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            form_name = form.cleaned_data['name']
            form_city = form.cleaned_data['city']
            #print name, description
            #post = m.Post.objects.create(content=content, created_at=created_at)
            return HttpResponseRedirect('hotels/')
 
    return render(request, 'main_app/post_form_upload.html', {
        'form': form,
    })