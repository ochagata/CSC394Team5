from django.conf.urls import patterns, url

from ARK import views

urlpatterns = patterns('',
    # ex: /ARK/
    url(r'^$', views.index, name='index'),

)