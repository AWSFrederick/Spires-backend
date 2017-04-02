from django.http import HttpResponse
import requests


def transform(request, coordinates):
    latitude, longitude = coordinates.split(',')
    print(latitude)
    print(longitude)
    url = 'https://epsg.io/trans?data={0},{1}&s_srs=4326&t_srs=102685'.format(longitude, latitude)
    json = requests.get(url)
    return HttpResponse(json)
