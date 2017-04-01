from django.http import HttpResponse
import requests


def list_maps(request):
    url = 'http://spires2.cityoffrederick.com/ArcGIS/rest/services/?f=json&pretty=true'
    maps = requests.get(url)
    services = []
    for map in maps.json()['services']:
        if map['type'] == 'MapServer':
            services.append('<a href="/export/map/%s">%s</a><br>' % ( map['name'], map['name'] ))
    return HttpResponse(services)

def export_map(request, map_name):
    url = 'http://spires2.cityoffrederick.com/ArcGIS/rest/services/maptorender/MapServer/export?bbox=1189970.24945014%2C637070.413482656%2C1210045.399164%2C645541.933225805&bboxSR=&layers=&layerdefs=&size=1600%2C1200&imageSR=&format=png&transparent=false&dpi=&time=&layerTimeOptions=&f=image'
    img = requests.get(url.replace('maptorender', map_name))
    return HttpResponse(img, content_type="image/png")

def status(request):
    return HttpResponse('Ok')
