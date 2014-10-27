from django.conf.urls import *
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'r2e2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'autho.views.login_user'),
    url(r'^login2/$', 'autho.views.logout_view')
)