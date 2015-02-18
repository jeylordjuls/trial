from django.conf.urls import patterns, include, url
from django.contrib import admin
from users import views
from rooms import views as views1
from reservations import views as views2


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'r2e2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls')),
    # url(r'^rooms/', include('rooms.urls')),
    # url(r'^reservations/', include('reservations.urls')),
    
    
)



# urlpatterns = patterns('',

#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^login/$', views.user_login, name='login'),
#     url(r'^logout/$', views.user_logout, name='logout'),
#     #url(r'^home/request_details/$', myviews.request_detail, name='add_request'),
#    url(r'^login/reservations/reservation_lists/$', views2.reservation_list, name='add_request'),
#    url(r'^reservations/reservation_lists1/$', views2.reservation_list1, name='add_request1'),
#    url(r'^users/user_lists/$', views.user_list, name='user_list'),  
#     url(r'^users/add_user/$', views.register, name='register'),
#     url(r'^reservations/add_reservation/$', views2.add_reserve, name='reservation'), 
#     url(r'rooms/add_room/$', views1.add_room, name='room'),
#     url(r'reservations/request_details/(?P<reserve_id>\w+)/$', views2.request_detail, name='request_detail')
# )
