# -*- coding: utf-8 -*-

from django.conf.urls import url
from snippets import views
    
urlpatterns = [
    url(r'^list/$', views.snippet_list),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
