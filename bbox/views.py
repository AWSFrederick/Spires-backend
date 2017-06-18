from django.http import HttpResponse
import requests
#from django.views.decorators.cache import cache_page


def transform(request, coordinates):
    first_latitude, first_longitude, second_latitude, second_longitude = coordinates.split(',')
    url = 'https://epsg.io/trans?data={0},{1};{2},{3}&s_srs=4326&t_srs=102685'.format(first_longitude, first_latitude, second_longitude, second_latitude)
    json_coordinates = requests.get(url)
    md_coordinates = []
    for json_coordinate in json_coordinates.json():
        md_coordinates.append(json_coordinate['x'])
        md_coordinates.append(json_coordinate['y'])
    return HttpResponse('{0}'.format('%2C'.join(md_coordinates)))

#@cache_page(60 * 60)
def transform_map(request, map, coordinates):
    first_latitude, first_longitude, second_latitude, second_longitude = coordinates.split(',')
    url = 'https://epsg.io/trans?data={0},{1};{2},{3}&s_srs=4326&t_srs=102685'.format(first_longitude, first_latitude, second_longitude, second_latitude)
    json_coordinates = requests.get(url)
    md_coordinates = []
    for json_coordinate in json_coordinates.json():
        md_coordinates.append(json_coordinate['x'])
        md_coordinates.append(json_coordinate['y'])
    bbox_loc = '{0}'.format('%2C'.join(md_coordinates))
    base_url = 'http://spires2.cityoffrederick.com/ArcGIS/rest/services/maptorender/MapServer/export?'
    size = '1600%2C1200'
    export_format = 'png'
    url = '{0}bbox={1}&size={2}&format={3}&transparent=false&f=image'.format(base_url, bbox_loc, size, export_format)
    img = requests.get(url.replace('maptorender', map))
    return HttpResponse(img, content_type="image/png")

#@cache_page(60 * 60)
def transform_map_json(request, map, coordinates):
    first_latitude, first_longitude, second_latitude, second_longitude = coordinates.split(',')
    url = 'https://epsg.io/trans?data={0},{1};{2},{3}&s_srs=4326&t_srs=102685'.format(first_longitude, first_latitude, second_longitude, second_latitude)
    json_coordinates = requests.get(url)
    md_coordinates = []
    for json_coordinate in json_coordinates.json():
        md_coordinates.append(json_coordinate['x'])
        md_coordinates.append(json_coordinate['y'])
    bbox_loc = '{0}'.format('%2C'.join(md_coordinates))
    base_url = 'http://spires2.cityoffrederick.com/ArcGIS/rest/services/maptorender/MapServer/export?'
    size = '1600%2C1200'
    export_format = 'svg'
    url = '{0}bbox={1}&size={2}&format={3}&transparent=false&f=pjson'.format(base_url, bbox_loc, size, export_format)
    json = requests.get(url.replace('maptorender', map))
    return HttpResponse(json)

#@cache_page(60 * 60)
def transform_map_kmz(request, map, coordinates):
    first_latitude, first_longitude, second_latitude, second_longitude = coordinates.split(',')
    url = 'https://epsg.io/trans?data={0},{1};{2},{3}&s_srs=4326&t_srs=102685'.format(first_longitude, first_latitude, second_longitude, second_latitude)
    json_coordinates = requests.get(url)
    md_coordinates = []
    for json_coordinate in json_coordinates.json():
        md_coordinates.append(json_coordinate['x'])
        md_coordinates.append(json_coordinate['y'])
    bbox_loc = '{0}'.format('%2C'.join(md_coordinates))
    base_url = 'http://spires2.cityoffrederick.com/ArcGIS/rest/services/maptorender/MapServer/export?'
    size = '1600%2C1200'
    export_format = 'svg'
    url = '{0}bbox={1}&size={2}&format={3}&transparent=false&f=kmz'.format(base_url, bbox_loc, size, export_format)
    kmz = requests.get(url.replace('maptorender', map))

    response = HttpResponse(content=kmz)
    response['Content-Type'] = 'application/kmz'
    response['Content-Disposition'] = 'attachment; filename="%s.kmz"' % 'export'
    return response
