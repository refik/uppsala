from django.conf.urls.defaults import *

urlpatterns = patterns('uppsala.shoutbox.views',
	(r'^addShout/$', 'addShout'),
)
