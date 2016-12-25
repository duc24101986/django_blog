from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
	## Post view
	url(r'^$', views.post_list, name='post_list'),

	url(r'^new$', views.post_new, name='post_new'),

	url(r'^(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),

	url(r'^(?P<post_id>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

	url(r'^(?P<post_id>[0-9]+)/delete/$', views.post_delete, name='post_delete'),

	url(r'^(?P<post_id>[0-9]+)/share/$', views.post_share, name='post_share'),

	## authentication
	# login / logout urls
	url(r'^login/$', auth_views.login, name='login'),

	url(r'^logout/$', auth_views.logout, name='logout'),

	url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),

	## User view
	url(r'^user$', views.user_list, name='user_list')

]