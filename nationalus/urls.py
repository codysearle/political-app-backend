from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'nationalus.views.home', name='home'),


    url(r'^', include('apps.leadership.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
