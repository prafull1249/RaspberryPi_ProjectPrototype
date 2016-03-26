import googlemaps
gmaps = googlemaps.Client(key='AIzaSyDe87TeZbkL-DN_CfttJGpYP-DhglaGz2k')
geocodeRes = gmaps.geocode('1050 south Stanley, p134, Tempe, Arizona')
l = geocodeRes[0]['location']
lat = l['lat']
longt = l['lng']


