from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
	## User profile view
	url(r'^$', views.user_profile_list, name='user_profile_list'),

	# url(r'^new$', views.user_new, name='user_new'),
	#
	url(r'^(?P<user_profile_id>[0-9]+)/$', views.user_profile_detail, name='user_profile_detail'),
	#
	# url(r'^(?P<user_profile_id>[0-9]+)/edit/$', views.user_profile_edit, name='user_profile_edit'),
	#
	# url(r'^(?P<user_profile_id>[0-9]+)/delete/$', views.user_profile_delete, name='user_profile_delete'),
	#
	# ## authentication
	# # login / logout urls
	# url(r'^login/$', auth_views.login, name='login'),
	#
	# url(r'^logout/$', auth_views.logout, name='logout'),
	#
	# url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),

]