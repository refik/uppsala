from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'uppsala.fileshare.views.index'),
	(r'^addFile/$', 'uppsala.fileshare.views.addFile'),
)
