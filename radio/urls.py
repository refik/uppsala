from django.conf.urls.defaults import *

urlpatterns = patterns('uppsala.radio.views',
    (r'^$', 'index'),
    (r'^new/$', 'new'),
    (r'^(?P<station_id>\S+)/$', 'detail'),
)
