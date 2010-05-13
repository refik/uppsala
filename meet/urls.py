from django.conf.urls.defaults import *

urlpatterns = patterns('uppsala.meet.views',
	(r'^(?P<meet_id>\d+)/$', 'detail'),
	(r'^(?P<meet_id>\d+)/result/$', 'result'),
	(r'^(?P<meet_id>\d+)/vote/$', 'vote'),
	(r'^create/$', 'create'),
	(r'^new/$', 'new'),
)

