from main_app.views import HotelsViewSet, CitiesViewSet, OwnersViewSet
from rest_framework import renderers
from main_app import views
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

hotels_list = HotelsViewSet.as_view({
    'get': 'list',
    #'post': 'create'
})
hotels_detail = HotelsViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    #'patch': 'partial_update',
    #'delete': 'destroy'
})

cities_list = CitiesViewSet.as_view({
    'get': 'list',
    #'post': 'create'
})
cities_detail = CitiesViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    #'patch': 'partial_update',
    #'delete': 'destroy'
})

owners_list = OwnersViewSet.as_view({
    'get': 'list',
    #'post': 'create'
})
owners_detail = OwnersViewSet.as_view({
    'get': 'retrieve',
    #'put': 'update',
    #'patch': 'partial_update',
    #'delete': 'destroy'
})


urlpatterns = [
    #url(r'^$', api_root),
    url(r'^$', hotels_list, name='hotels-list'),
    url(r'^(?P<pk>[0-9]+)/$', hotels_detail, name='hotels-detail'),
    url(r'^cities/$', cities_list, name='cities-list'),
    url(r'^cities/(?P<pk>[0-9]+)/$', cities_detail, name='cities-detail'),
    url(r'^owners/$', owners_list, name='owners-list'),
    url(r'^owners/(?P<pk>[0-9]+)/$', owners_detail, name='owners-detail'),
]
