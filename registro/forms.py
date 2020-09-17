# -*- coding: utf-8 -*-
from django import forms
from registro.models import Certificado, Data


class DataForm(forms.ModelForm):
    """
    Formulario de la data que se sube al servidor.
    """
    class Meta:
        model = Data
        fields = ('descripcion','data_zip')


class CertificadoForm(forms.ModelForm):
    """
    Formulario del certificado digital que se sube al servidor.
    """
    class Meta:
        model = Certificado
        fields = ('nombre_completo','cedula','evento_curso','rol','certificado','uploaded_at')
