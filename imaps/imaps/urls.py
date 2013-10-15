from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'imaps.views.home', name='home'),
    url(r'^imaps/wwatch/', include('wwatch.urls')),
    url(r'^imaps/print-tracker/', include('print_tracker.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
