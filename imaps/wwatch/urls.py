from django.conf.urls.defaults import *
from django.conf import settings
from views import init, getEvents

urlpatterns = patterns('',
    url(r'^$', init, name='wwatch-home'),
    url(r'^json/Events$', getEvents),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
