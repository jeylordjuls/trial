from django.conf.urls import patterns, url
from rooms import views

urlpatterns = patterns('',
	 url(r'^add_room/$', views.add_room, name='add_room'),
)
