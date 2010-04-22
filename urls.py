from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^shouts/', include('uppsala.shoutbox.urls')),
	(r'^meet/', include('uppsala.meet.urls')),
	(r'^admin/', include(admin.site.urls)),
	(r'^comments/', include('django.contrib.comments.urls')),
)
