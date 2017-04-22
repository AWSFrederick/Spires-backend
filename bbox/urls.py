from django.conf.urls import url
from bbox import views

urlpatterns = [
    #url(r'coordinates=(.*)/', views.transform, name='transform'),
    url(r'^map/(.*)/coordinates=(.*)/', views.transform_map, name='transform_map'),
    url(r'^json/(.*)/coordinates=(.*)/', views.transform_map_json, name='transform_map_json'),
    url(r'^kmz/(.*)/coordinates=(.*)/', views.transform_map_kmz, name='transform_map_kmz')
]
