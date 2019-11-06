from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('index/',views.index, name='index'),
    path('api_topo/',views.api_topo,name='api_topo'),
    url(r'^ajax_neighbor/$',views.ajax_neighbor,name='ajax_neighbor'),
]
