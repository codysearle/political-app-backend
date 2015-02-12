__author__ = 'nicky'

from django.conf.urls import patterns, include, url

urlpatterns = patterns (
    '',

    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),

)