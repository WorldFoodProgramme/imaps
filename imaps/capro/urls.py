from django.conf.urls.defaults import *
from django.conf import settings
import capro.views as capro

urlpatterns = patterns('',
	url(r'^/?$', capro.init, name='capro-home'),
	url(r'^json/?$', capro.JSONSerializer, name='capro-country-json'),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
