from django.conf.urls import url, include
from main_app import views
import main_app
from rest_framework.routers import DefaultRouter
from django.contrib import admin

router = DefaultRouter()
router.register(r'hotels', views.HotelsViewSet)
router.register(r'owners', views.OwnersViewSet)
router.register(r'cities', views.CitiesViewSet)
router.register(r'reviews', views.ReviewsViewSet)
router.register(r'search/hotels', views.SearchHotelsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^search/',
        views.post_form_upload, name='post_form_upload'),
    url(r'^admin/', include(admin.site.urls)),
]
