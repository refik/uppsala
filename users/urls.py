from django.conf.urls.defaults import *

urlpatterns = patterns('uppsala.users.views',
	(r'^$', 'chat'),
	(r'^wave/$', 'wave'),
	(r'^login_page/$', 'login_page'),
	(r'^login/$', 'login_user'),
	(r'^logout/$', 'logout_view'),
	(r'^register/$', 'register'),
)

