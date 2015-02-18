from django.conf.urls import patterns, url
from reservations import views

urlpatterns = patterns('',
   url(r'^reservation_lists/$', views.reservation_list, name='add_request'),
   url(r'^reservation_lists1/$', views.reservation_list1, name='add_request1'),
   url(r'^add_reservation/$', views.add_reserve, name='reservation'),
   url(r'^request_details/(?P<reserve_id>\w+)/$', views.request_detail, name='request_detail'),
)
