from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2efdd48d83184d8b795bc2fe9bc4cb437e2a5685
	(r'^shouts/', include('uppsala.shoutbox.urls')),
	(r'^meet/', include('uppsala.meet.urls')),
	(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
=======
    (r'^shouts/', include('uppsala.shoutbox.urls')),
    (r'^meet/', include('uppsala.meet.urls')),
    (r'^admin/', include(admin.site.urls)),
>>>>>>> a338b894e4ed9ccdc497c33e6e34af04859b56a3
=======
	(r'^users/', include('uppsala.users.urls')),
	(r'^comments/', include('django.contrib.comments.urls')),
>>>>>>> 2efdd48d83184d8b795bc2fe9bc4cb437e2a5685
)
