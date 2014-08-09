from django.conf.urls import patterns, url

from info import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='info.index'),
    url(r'^list/(\d+)$', views.list, name='info.list'),
    url(r'^detail/(\d+)$', views.detail, name='info.detail')
)
