from django.conf.urls import patterns, include, url
from django.contrib import admin
from manager import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^controller/', include('controller.urls')),
    url(r'^$', include('controller.urls')),
    url(r'^static/(.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT} ),
)
