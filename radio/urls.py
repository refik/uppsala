from django.conf.urls.defaults import *

urlpatterns = patterns('uppsala.radio.views',
    (r'^$', 'index'),
    (r'^new/$', 'new'),
    (r'^(?P<station_id>\S+)/$', 'detail'),
    (r'^(?P<poll_id>\d+)/vote/$', 'vote'),
    (r'^create/$', 'create'),
)
