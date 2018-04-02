# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Certificado(models.Model):
    cedula = models.CharField(max_length=255, blank=True, null=True)
    certificado = models.FileField(upload_to='', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __unicode__(self):
        return self.descripcion
