from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    url(r'^$', views.init, name='home-critical-elections'),
    url(r'^json/(?P<object>\w+)/?$', views.JSONSerializer),
)

