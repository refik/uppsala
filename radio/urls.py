from django.conf.urls.defaults import *

urlpatterns = patterns('uppsala.radio.views',
    (r'^new/$', 'new'),
    (r'^restart$', 'restart'),
    (r'^(?P<station_id>\S+)/$', 'detail'),
)
