# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from registro import views
from registro.views import *
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    #url(r'^$', Index.as_view(), name='index'),
    url(r'^$', buscar, name='buscar'),
    url(r'^lista_certificados$', login_required(views.Lista_Certificados.as_view()), name='lista_certificados'),
    url(r'^subir_data$', login_required(views.Subir_data.as_view()), name='subir_data'),
    url(r'^subir_data_csv$', login_required(views.Subir_data_csv.as_view()), name='subir_data_csv'),
    url(r'^guardar_certificado$', login_required(views.Guardar_Certificado.as_view()), name='guardar_certificado'),
    url(r'^editar_certificado/(?P<pk>\d+)$', login_required(views.Editar_Certificado.as_view()), name='editar_certificado'),
    url(r'^borrar_certificado/(?P<pk>\d+)$', login_required(views.Borrar_Certificado.as_view()), name='borrar_certificado'),
    # Definiendo la url que va a servir los certificados para que puedan ser descargados.
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    # Definiendo la url que va a servir los certificados para que puedan ser descargados luego de filtrar.
    url(r'^busqueda/media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^descomprimir_zip$', login_required(descomprimir_zip), name='descomprimir_zip'),
    url(r'^insertar_csv$', login_required(insertar_csv), name='insertar_csv'),
    url(r'^busqueda/$', busqueda, name='busqueda'),
    url(r'^salir$', login_required(views.Salir.as_view()), name='salir'),
)
