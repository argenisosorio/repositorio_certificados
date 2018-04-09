# -*- coding: utf-8 -*-
from django import forms
from registro.models import Certificado


class CertificadoForm(forms.ModelForm):
    class Meta:
        model = Certificado
        fields = ('nombre_completo','cedula','evento_curso','rol','certificado')
