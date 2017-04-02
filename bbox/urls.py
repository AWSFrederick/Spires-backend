from django.conf.urls import url
from bbox import views

urlpatterns = [
    url(r'coordinates=(.*)/', views.transform, name='transform')
]
