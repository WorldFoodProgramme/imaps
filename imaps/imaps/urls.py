from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 
        TemplateView.as_view(template_name='index.html'),
        name='index'),
    url(r'^smartfeeds/', include('smart_feeds.urls')),
    url(r'^wwatch/', include('wwatch.urls')),
    url(r'^capro/', include('capro.urls')),
    url(r'^print-tracker/', include('print_tracker.urls')),
    url(r'^gis-presence/', TemplateView.as_view(template_name='gis_presence/employees-map.html'), 
        name='gis-presence'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_export/', include('admin_export.urls')),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
