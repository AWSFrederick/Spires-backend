from django.http import HttpResponse
import requests

def list_maps(request):
    url = 'http://spires2.cityoffrederick.com/ArcGIS/rest/services/?f=json&pretty=true'
    maps = requests.get(url)
    print(maps.json())
    return HttpResponse(maps)

def test(request):
    return HttpResponse('Ok')
