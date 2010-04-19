from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^shouts/$', include('uppsala.shoutbox.urls')),
    (r'^admin/', include(admin.site.urls)),
)
