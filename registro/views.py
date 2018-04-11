# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from registro.models import Certificado, Data
from registro.forms import CertificadoForm, DataForm
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render_to_response


class Subir_data(SuccessMessageMixin, CreateView):
    """
    Clase que permite subir la data .zip en el servidor.
    """
    model = Data
    form_class = DataForm
    template_name = "registro/subir_data.html"
    success_url = reverse_lazy('registro:subir_data')
    success_message = "La data se guardo con éxito"


class Guardar_Certificado(SuccessMessageMixin, CreateView):
    """
    Clase que permite guardar los certificados, se guardar en /media.
    """
    model = Certificado
    form_class = CertificadoForm
    template_name = "registro/guardar_certificado.html"
    success_url = reverse_lazy('registro:buscar')
    success_message = "Se guardo el certificado con éxito"


class Lista_Certificados(ListView):
    """
    Clase que permite listar los certificados registrados.
    """
    model = Certificado
    template_name = "registro/lista_certificados.html"


class Editar_Certificado(SuccessMessageMixin, UpdateView):
    """
    Clase que permite editar los certificados registrados.
    """
    template_name = "registro/guardar_certificado.html"
    form_class = CertificadoForm
    model = Certificado
    success_message = "Se actualizó la información con éxito"
    success_url = reverse_lazy('registro:lista_certificados')


class Borrar_Certificado(SuccessMessageMixin, DeleteView):
    """
    Clase que permite borrar los certificados.
    """
    form_class = CertificadoForm
    model = Certificado
    success_message = "Se eliminó la información con éxito"
    success_url = reverse_lazy('registro:lista_certificados')


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
        if certificados:
            return render(request, 'registro/buscar.html',  {'certificados': certificados, 'query': q})
        else:
            messages = ['No se encontró ningún certificado.']
            return render_to_response('registro/buscar.html', {'messages': messages})
    else:
        messages = ['Por favor introduce una cédula de identidad.']
        return render_to_response('registro/buscar.html', {'messages': messages})


class Salir(View):
    """
    Clase que permite cerrar la sesión de usuario.
    """

    def get(self, request):
        """
        Método que redireccíona cuando se cierra la sesión.
        """
        logout(request)
        return redirect('/')
