from django.conf.urls import patterns, url

from ARK import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # ex: /ARK/
    url(r'^profile/$', 'ARK.views.profile'),

    url(r'^$', views.index, name='index'),
)
