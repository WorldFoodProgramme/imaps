from django.conf.urls.defaults import *
import capro.views as capro

urlpatterns = patterns('',
	url(r'^/?$', capro.init, name='capro-home'),
	url(r'^json/?$', capro.JSONSerializer, name='capro-country-json'),
)

