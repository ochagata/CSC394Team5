from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from Pazzos import views

urlpatterns = patterns('',
    url(r'^ARK/', include('ARK.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Pazzos/', views.index)
)
