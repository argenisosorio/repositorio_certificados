# -*- coding: utf-8 -*-
import os
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.http import JsonResponse


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('registro.urls', namespace='registro')),
    # Devolver la versión del software.
    url(r'^version/$',
        lambda request: JsonResponse({
            'version': open(os.path.join(settings.BASE_DIR, 'VERSION.txt')).read().strip()
        }),
        name='version'),
]
