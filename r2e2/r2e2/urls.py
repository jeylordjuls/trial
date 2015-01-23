from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts import views
from home import views as myviews

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    #url(r'^home/request_details/$', myviews.request_detail, name='add_request'),
   url(r'^home/reservation_lists/$', myviews.reservation_list, name='add_request'),
   url(r'^home/reservation_lists1/$', myviews.reservation_list1, name='add_request1'),
   url(r'^home/user_lists/$', myviews.user_list, name='user_list'),  
    url(r'^home/add_user/$', views.register, name='register'),
    url(r'^home/add_reservation/$', views.add_reserve, name='reservation'), 
    url(r'home/add_room/$', views.add_room, name='room'),
    url(r'home/request_details/(?P<reserve_id>\w+)/$', myviews.request_detail, name='request_detail')
)
