from django.conf.urls.defaults import *

urlpatterns = patterns('uppsala.fileshare.views',
	(r'^addFile/$', 'addFile'),
)
