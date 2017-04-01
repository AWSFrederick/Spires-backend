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
    # $ curl "https://epsg.io/trans?data=-77.430311,39.465278;-77.379034,39.447878&s_srs=4326&t_srs=102685" | jq -r '.[]'
    base_url = 'http://spires2.cityoffrederick.com/ArcGIS/rest/services/maptorender/MapServer/export?'
    bbox_loc = '1189970.24945014%2C637070.413482656%2C1210045.399164%2C645541.933225805'
    size = '1600%2C1200'
    export_format = 'png'

    url = '{0}bbox={1}&size={2}&format={3}&transparent=false&f=image'.format(base_url, bbox_loc, size, export_format)
    img = requests.get(url.replace('maptorender', map_name))
    return HttpResponse(img, content_type="image/png")

def status(request):
    return HttpResponse('Ok')
