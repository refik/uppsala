from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^addFile/$', 'uppsala.fileshare.views.addFile'),
	(r'^addRadioFile/(?P<station>\S+)/$', 'uppsala.fileshare.views.addRadioFile'),
)
