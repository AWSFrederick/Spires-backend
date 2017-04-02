from django.conf.urls import url
from bbox import views

urlpatterns = [
    #url(r'coordinates=(.*)/', views.transform, name='transform'),
    url(r'^map/(.*)/coordinates=(.*)/', views.transform_map, name='transform_map')
]
