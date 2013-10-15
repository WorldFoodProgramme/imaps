from django.conf.urls.defaults import *
import views

from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
   	(r'^admin/', include(admin.site.urls)),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/opt/odep/static'}),
	(r'^/?$', views.init),
	(r'^report/(?P<year>\d{4})/?$', views.mapReport),
	(r'^report/(?P<year>\d{4})/(?P<month>\d+)/?$', views.mapReport),
	(r'^report/(?P<unit>\w+-*\w*)/?$', views.mapReport),
	(r'^report/(?P<unit>\w+-*\w*)/(?P<year>\d+)/?$', views.mapReport),
	(r'^report/(?P<unit>\w+-*\w*)/(?P<year>\d+)/(?P<month>\d+)/?$', views.mapReport),
	(r'^units/?$', views.getUnits),
	(r'^years/?$', views.getYears),
)
