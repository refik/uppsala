from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< HEAD
	(r'^shouts/', include('uppsala.shoutbox.urls')),
	(r'^admin/', include(admin.site.urls)),
=======
    (r'^shouts/', include('uppsala.shoutbox.urls')),
    (r'^meet/', include('uppsala.meet.urls')),
    (r'^admin/', include(admin.site.urls)),
>>>>>>> a338b894e4ed9ccdc497c33e6e34af04859b56a3
)
