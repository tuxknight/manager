#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from controller import views
from django.contrib import admin
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.list),
    url(r'^index/$', views.list),
    url(r'^add/$', views.add),
    #url(r'^add/$', include(admin.site.urls)),
    url(r'^list/$', views.list),
    url(r'^device/$', views.device),
    url(r'^commit/$', views.commit),
    url(r'^log/$', views.log)
)

