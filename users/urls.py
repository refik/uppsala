from django.conf.urls.defaults import *

urlpatterns = patterns('uppsala.users.views',
                       (r'^$', 'index'),
                       (r'^login/$', 'login_user'),
                       (r'^logout/', 'logout'),
                       (r'^register/', 'register'),

)

