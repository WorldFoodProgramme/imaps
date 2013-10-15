#from tools import extents
#from flood.views import alerted_countries
#extent = extents.countryExtent("Haiti")
#c = alerted_countries()
#print extent
#print c

import json
from django.contrib.gis.geos import GEOSGeometry
#from haiti.models import  Houses


geojson_in = '{"type":"Polygon", "coordinates":[[[-8112483.1169887, 2133747.1101526], [-8063563.4188949, 2148117.2714677], [-8113094.6132148, 2173800.1129669], [-8113094.6132148, 2174717.3573062], [-8112483.1169887, 2133747.1101526]]]}, "crs":{"type":"EPSG", "properties":{"code":900913}}'
#json_array = geojson_in.split(';')
#json_array.pop()
#for element in json_array:
	#print json.loads(element)
	
a = GEOSGeometry(geojson_in)
print a
#house = Houses(geom=GEOSGeometry(geojson_in))
#house.save()