# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'front/index.html'}, name='index'),
    url(r'^short/$', 'short.views.short', name='short'),
    url(r'^(?P<codigo>\w+)/$', 'short.views.view', name='view'),
)