# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from registro.models import Certificado
from registro.forms import CertificadoForm
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect


class Guardar_Certificado(SuccessMessageMixin,CreateView):
    """
    Clase que permite guardar los certificados, se guardar en /media
    """
    model = Certificado
    form_class = CertificadoForm
    template_name = "registro/guardar_certificado.html"
    success_url = reverse_lazy('registro:buscar')
    success_message = "Se guardo el certificado con éxito"


class Lista_Certificados(ListView):
    """
    Clase que permite listar los certificados registrados
    """
    model = Certificado
    template_name = "registro/lista_certificados.html"


def buscar(request):
    """
    Función que muestra la plantilla con el formulario de búsqueda.
    """
    return render(request, 'registro/buscar.html')


def busqueda(request):
    """
    Función que permite hacer el query con los certificados ya filtrados.
    """
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        certificados = Certificado.objects.filter(cedula__icontains=q)
        return render(request, 'registro/buscar.html',  {'certificados': certificados, 'query': q})
    else:
        return HttpResponse('Por favor introduce un termino de búsqueda.')
