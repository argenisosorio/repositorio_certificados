# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Data(models.Model):
    """
    Modelo de la data que se sube al servidor.
    """
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    data_zip = models.FileField(upload_to='', blank=True, null=True)

    def __unicode__(self):
        return self.descripcion


class Certificado(models.Model):
    """
    Modelo del certificado digital que se sube al servidor.
    """
    nombre_completo = models.CharField(max_length=255, blank=True, null=True)
    cedula = models.CharField(max_length=255, blank=True, null=True)
    evento_curso = models.CharField(max_length=255, blank=True, null=True)
    rol = models.CharField(max_length=255, blank=True, null=True)
    certificado = models.FileField(upload_to='', blank=True, null=True)
    uploaded_at = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('registro:editar_certificado', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.cedula
