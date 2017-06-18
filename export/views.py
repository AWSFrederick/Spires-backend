from django.http import HttpResponse, HttpResponseNotFound
import requests
#from django.views.decorators.cache import cache_page

#@cache_page(60 * 60)
def list_maps(request):
    url = 'http://spires2.cityoffrederick.com/ArcGIS/rest/services/?f=json&pretty=true'
    maps = requests.get(url)
    services = []
    for map in maps.json()['services']:
        if map['type'] == 'MapServer':
            services.append('%s\n' % map['name'])
    return HttpResponse(services)

def status(request):
    return HttpResponse('Ok')

def reststatus(request):
    url = 'http://spires2.cityoffrederick.com/ArcGIS/rest/services/?f=json&pretty=true'
    maps = requests.get(url)
    if maps:
        print('Testing Spires2 endpoint')
        return HttpResponse('Ok')
    else:
        return HttpResponseNotFound('Spires2 endpoint is down')
