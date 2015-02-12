__author__ = 'nicky'

from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns(
    '',

    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^users$', UserList.as_view(), name='user-list'),


)