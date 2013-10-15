from django.contrib import admin
from models import *

class InlineCopy(admin.TabularInline):
	"""
	Defined the Copy entities to be displayed together with their map in the Map admin page
	"""
	model = Copy
	
class MapAdmin(admin.ModelAdmin):
	"""
	Defines the layout of the Map admin page
	"""
	inlines = [InlineCopy,]
	list_display = ('title','file_name','last_updated')
	fieldsets = (
		(None,{
			'fields': ('title','file_name','date_completed','last_updated','type','status','print_format','author_contact',)
		}),
		('Uploads',{
			'fields': ('up_odep','up_back','up_epweb','up_vam',)
		}),
		(None,{
			'fields': ('remarks',)
		})        
	)
	search_fields = ('title','file_name',)
	list_filter = ('date_completed','print_format','type',)
	ordering = ('date_completed',)
	
admin.site.register(Map,MapAdmin)
admin.site.register(Format)
admin.site.register(Unit)