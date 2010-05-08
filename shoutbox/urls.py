from django.conf.urls.defaults import *

urlpatterns = patterns('uppsala.shoutbox.views',
	(r'^$', 'index'),
	(r'^addShout/$', 'addShout'),
)
