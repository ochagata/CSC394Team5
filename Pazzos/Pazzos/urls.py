from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^accounts/login/$', 'ARK.views.login'),
    url(r'^accounts/logout/$', 'ARK.views.logout'),
    url(r'^accounts/auth/$', 'ARK.views.auth_view'),
    url(r'^accounts/loggedin/$', 'ARK.views.loggedin'),
    url(r'^accounts/register/$', 'ARK.views.register'),
    url(r'^accounts/register_success/$', 'ARK.views.register_success'),
    url(r'^accounts/profile/$', 'ARK.views.profile'),

    url(r'^ARK/', include('ARK.urls')),
    url(r'^admin/', include(admin.site.urls)),

)