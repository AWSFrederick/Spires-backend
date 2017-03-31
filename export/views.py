from django.http import HttpResponse
import requests
import pprint

def list_maps(request):
    url = 'http://spires2.cityoffrederick.com/ArcGIS/rest/services/?f=json&pretty=true'
    maps = requests.get(url)
    services = []
    for map in maps.json()['services']:
        if map['type'] == 'MapServer':
            services.append('<a href="/export/map/%s">%s</a><br>' % ( map['name'], map['name'] ))
    return HttpResponse(services)

def test(request):
    return HttpResponse('Ok')
