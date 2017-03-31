from django.conf.urls import url
from export import views

urlpatterns = [
    url(r'^$', views.list_maps, name='export_list_maps'),
    url(r'^map/(.*)/$', views.export_map, name='export_map'),
    url(r'^test/$', views.test, name='export_test')
]
