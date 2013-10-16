from django.contrib.gis import admin
from django.contrib import admin as stdAdmin
from models import *

#admin.site.register(Country, admin.GeoModelAdmin)
#admin.site.register(Country, admin.OSMGeoAdmin)

class ElectionInline(admin.TabularInline):
    model = Election
    extra = 0

class UpdateInline(admin.TabularInline):
    model = Update
    extra = 0

class CountryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Country',       {'fields': ['terr_name']}),
    ]
    inlines = [ElectionInline]
    list_display = ['terr_name']
    #list_filter = ['status']
    search_fields = ['terr_name']

class ElectionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Election',       {'fields': ['election_type', 'election_date_start', 'election_date_text', 'election_date_end', 'election_comment']}),
    ]
    inlines = [UpdateInline]
    list_display = ('country', 'election_type', 'election_date_start', 'election_date_end')
    list_filter = ('election_type', 'election_date_start', 'election_date_end')
    search_fields =  ['country__terr_name', 'election_type']

admin.site.register(Country, CountryAdmin)
admin.site.register(Election, ElectionAdmin)
