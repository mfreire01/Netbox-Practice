from django.conf.urls import include, url
from django.contrib import admin
from django.views.defaults import page_not_found

from views import home, trigger_500
from users.views import login, logout


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^circuits/', include('circuits.urls', namespace='circuits')),
    url(r'^dcim/', include('dcim.urls', namespace='dcim')),
    url(r'^ipam/', include('ipam.urls', namespace='ipam')),
    url(r'^secrets/', include('secrets.urls', namespace='secrets')),
    url(r'^profile/', include('users.urls', namespace='users')),

    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^api/circuits/', include('circuits.api.urls', namespace='circuits-api')),
    url(r'^api/dcim/', include('dcim.api.urls', namespace='dcim-api')),
    url(r'^api/ipam/', include('ipam.api.urls', namespace='ipam-api')),
    url(r'^api/secrets/', include('secrets.api.urls', namespace='secrets-api')),
    url(r'^api/docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Error testing
    url(r'^404/$', page_not_found),
    url(r'^500/$', trigger_500),

    url(r'^admin/', include(admin.site.urls)),
]
