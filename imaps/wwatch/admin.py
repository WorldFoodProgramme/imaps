from django.contrib.gis import admin
from django.contrib import admin as stdAdmin
from models import *

#admin.site.register(Country, admin.GeoModelAdmin)
#admin.site.register(Country, admin.OSMGeoAdmin)

class InlineResource(admin.TabularInline):
	model = Resource

class InlineLink(admin.TabularInline):
	model = Link

class EventInline(admin.TabularInline):
    model = Event
    inlines = [InlineResource, InlineLink,]
    extra = 0

class CountryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Country',       {'fields': ['terr_name']}),
    ]
    #inlines = [EventInline]
    list_display = ['terr_name']
    #list_filter = ['status']
    search_fields = ['terr_name']

class EventAdmin(admin.ModelAdmin):
    inlines = [InlineResource, InlineLink,]
    fieldsets = [
        ('Event',{'fields': ['country', 'date', 'alert_level', 'hazard_type', 'confidence', 'event_comment', 'visible' ]}),
    ]
    
    list_display = ('country', 'alert_level', 'hazard_type', 'event_comment', 'date', 'visible')
    list_filter = ('country', 'alert_level', 'hazard_type', 'date')
    search_fields =  ['country__terr_name', 'alert_level']

admin.site.register(Country, CountryAdmin)
admin.site.register(Event, EventAdmin)
