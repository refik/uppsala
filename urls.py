from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< HEAD:urls.py
    (r'^shouts/', include('uppsala.shoutbox.urls')),
    (r'^meet/', include('uppsala.meet.urls')),
    (r'^admin/', include(admin.site.urls)),
=======

>>>>>>> a87db55bcf0b61b00b5f12327cd6de6400777a98:urls.py
)
