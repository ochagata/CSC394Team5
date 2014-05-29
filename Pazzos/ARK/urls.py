from django.conf.urls import patterns, url

from ARK import views

urlpatterns = patterns('',
    # ex: /ARK/
    url(r'^profile/$', 'ARK.views.profile'),

    url(r'^$', views.index, name='index'),
)
