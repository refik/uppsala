from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'uppsala.shoutbox.views.index'),
)
