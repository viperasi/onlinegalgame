from django.conf.urls.defaults import patterns, url
from . import views

urlpatterns = patterns('role.views',
    url(r'^list/$',
		views.role_list, 
		name='role_list'),

    url(r'^add/$', 
		views.add_role, 
		name='add_role'),

    url(r'^edit/(?P<role_id>\d+)/$', 
		views.edit_role, 
		name='edit_role'),
        
    url(r'^show/(?P<role_id>\d+)/$', 
		views.show_role, 
		name='show_role'),

    url(r'^link/$', 
        views.link_role, 
        name='link_role'),
        
    url(r'^unlink/$', 
        views.unlink_role, 
        name='unlink_role'),
	)
