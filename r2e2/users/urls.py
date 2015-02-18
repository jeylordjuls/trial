from django.conf.urls import patterns, url, include
from users import views
from reservations import views as myviews

urlpatterns = patterns('',
	url(r'^login', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^rooms/', include('rooms.urls')),
    url(r'^reservations/', include('reservations.urls')),	
    url(r'^user_lists', views.user_list, name='user_list'),  
    url(r'^add_user/$', views.register, name='register'),
)