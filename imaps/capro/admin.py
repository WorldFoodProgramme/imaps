from django.contrib.gis import admin
from django.contrib import admin as stdAdmin
from models import *

class InlineProfile(admin.TabularInline):
	model = Profile

class CountryAdmin(admin.OSMGeoAdmin):	
	default_lon = 0
	default_lat = 0
	default_zoom = 3
	extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js','http://code.jquery.com/jquery-1.4.2.min.js']
	inlines = [InlineProfile,]
	fieldsets = (
		(None,{
			'fields': ('name','regional','ndmo','reporting_line','address','focal_point','contacts','wfp_focal_point',)
		}),
		('Geographic',{
			'fields': ('point',)
		}),        
	)	
	

admin.site.register(Country,CountryAdmin)
