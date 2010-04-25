from django.conf.urls.defaults import *
from uppsala.settings import PROJECT_PATH, DEBUG
from django.contrib import admin
admin.autodiscover()

media_path =  PROJECT_PATH+'/media'
#print media_path
urlpatterns = patterns('',
	(r'^shouts/', include('uppsala.shoutbox.urls')),
	(r'^meet/', include('uppsala.meet.urls')),
	(r'^admin/', include(admin.site.urls)),
	(r'^users/', include('uppsala.users.urls')),
	(r'^', include('uppsala.users.urls')),
	(r'^fileshare/', include('uppsala.fileshare.urls')),
	(r'^comments/', include('django.contrib.comments.urls')),

)

# Media Folder (for the development phase. Should be deleted after)
if DEBUG:
	urlpatterns += patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s/media' % PROJECT_PATH}),
	)

