from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/opt/odep/static'}),
	url(r'^/?$', views.init, name='print-tracker-home'),
	(r'^report/(?P<year>\d{4})/?$', views.mapReport),
	(r'^report/(?P<year>\d{4})/(?P<month>\d+)/?$', views.mapReport),
	(r'^report/(?P<unit>\w+-*\w*)/?$', views.mapReport),
	(r'^report/(?P<unit>\w+-*\w*)/(?P<year>\d+)/?$', views.mapReport),
	(r'^report/(?P<unit>\w+-*\w*)/(?P<year>\d+)/(?P<month>\d+)/?$', views.mapReport),
	(r'^units/?$', views.getUnits),
	(r'^years/?$', views.getYears),
)
