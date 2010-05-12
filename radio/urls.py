from django.conf.urls.defaults import *

urlpatterns = patterns('uppsala.radio.views',
    (r'^new/$', 'new'),
    (r'^(?P<station_id>\S+)/$', 'detail'),
	 (r'^restart/(?P<station_id>\S+)/$', 'restart'),
)
