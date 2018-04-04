# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from registro import views
from registro.views import *
from django.conf import settings


urlpatterns = patterns('',
    #url(r'^$', Index.as_view(), name='index'),
    url(r'^lista_certificados$', views.Lista_Certificados.as_view(), name='lista_certificados'),
    url(r'^guardar_certificado$', views.Guardar_Certificado.as_view(), name='guardar_certificado'),
    url(r'^editar_certificado/(?P<pk>\d+)$', views.Editar_Certificado.as_view(), name='editar_certificado'),
    url(r'^borrar_certificado/(?P<pk>\d+)$', views.Borrar_Certificado.as_view(), name='borrar_certificado'),
    # Definiendo la url que va a servir los certificados para que puedan ser descargados.
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    # Definiendo la url que va a servir los certificados para que puedan ser descargados luego de filtrar.
    url(r'^busqueda/media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^$', buscar, name='buscar'),
    url(r'^busqueda/$', busqueda, name='busqueda'),
)
