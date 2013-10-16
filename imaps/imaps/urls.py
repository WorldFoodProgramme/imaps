from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 
        TemplateView.as_view(template_name='index.html'),
        name='index'),
    url(r'^imaps/smartfeeds/', include('smart_feeds.urls')),
    url(r'^imaps/wwatch/', include('wwatch.urls')),
    url(r'^imaps/print-tracker/', include('print_tracker.urls')),
    url(r'^imaps/critical-elections/', include('critical_election.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

