# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Certificado(models.Model):
    nombre_completo = models.CharField(max_length=255, blank=True, null=True)
    cedula = models.CharField(max_length=255, blank=True, null=True)
    evento_curso = models.CharField(max_length=255, blank=True, null=True)
    certificado = models.FileField(upload_to='', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('registro:editar_certificado', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.cedula
