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
from django.template import RequestContext
from datetime import datetime
import os
import csv
from django.db.models import Max


class Subir_data(SuccessMessageMixin, CreateView):
    """
    Clase que permite subir la data .zip en el servidor.
    """
    model = Data
    form_class = DataForm
    template_name = "registro/subir_data.html"
    success_url = reverse_lazy('registro:subir_data')
    success_message = "La data se guardo con éxito"

    def post(self, request, *args, **kwargs):
        self.object = None
        #print "----------------"
        #print "Entro en el método post de Subir_data"
        #print "----------------"
        #a = os.getcwd()
        #print a
        #os.chdir(a+'/media/')
        #os.system("ls -l")
        #print "Listo el contenido del directorio"
        return super(Subir_data, self).post(request, *args, **kwargs)


class Subir_data_csv(SuccessMessageMixin, CreateView):
    """
    Clase que permite subir la data .csv en el servidor.
    """
    model = Data
    form_class = DataForm
    template_name = "registro/subir_data_csv.html"
    success_url = reverse_lazy('registro:subir_data')
    success_message = "La data se guardo con éxito"

    def post(self, request, *args, **kwargs):
        self.object = None
        return super(Subir_data_csv, self).post(request, *args, **kwargs)


def descomprimir_zip(request):
    """
    Función que sirve para descomprimir y luego borrar el .zip adjuntado
    anteriormente.
    """
    a = os.getcwd() # Guardar el directorio actual en la variable a.
    #os.chdir(a+'/media') # Cambiarse a /media desde la raíz del proyecto.
    os.chdir(settings.MEDIA_ROOT) # Cambiarse a /media desde la raíz del proyecto.
    os.system("unzip *.zip") # Descomprimir todos los .zip del directorio.
    os.system("rm *.zip") # Remover todos los .zip del directorio.
    os.chdir(a) # Cambiarse al directorio raíz del proyecto.
    messages = ['¡Se descomprimió el .zip con éxito y luego se borró el .zip!']
    return render_to_response('registro/buscar.html', {'messages': messages}, context_instance=RequestContext(request))


def insertar_csv(request):
    """
    Función que permite insertar la data .csv en la base de datos sqlite.
    """
    a = os.getcwd() # Guardar el directorio actual en la variable a.
    #os.system("bash insert_csv.sh") # Ejecutar el script en bash.
    os.system("bash insert_csv.sh %s %s" % (settings.MEDIA_ROOT, settings.DATABASES['default']['NAME'])) # Ejecutar el script en bash.
    os.chdir(a) # Cambiarse al directorio raíz del proyecto.
    messages = ['¡Se insertó la data .csv correctamente!']
    return render_to_response('registro/buscar.html', {'messages': messages}, context_instance=RequestContext(request))


def insertar_data_csv(request, template_name='registro/lista_certificados.html'):
    """
    Función que permite insertar los datos del fichero CSV en la base de datos.
    """
    with open(settings.MEDIA_ROOT+'/data_final.csv', 'r') as listado:
        datos = csv.reader(listado, delimiter=',') # Separar la data por coma.
        for row in datos:
            nombre_completo = row[0]
            cedula = row[1]
            evento_curso = row[2]
            rol = row[3]
            certificado = row[4]
            uploaded_at = row[5]
            Certificado.objects.create(nombre_completo=nombre_completo, cedula=cedula, evento_curso=evento_curso, rol=rol, certificado=certificado,uploaded_at=uploaded_at)
    listado.close()
    a = os.getcwd() # Guardar el directorio actual en la variable a.
    os.system("bash delete_csv.sh %s %s" % (settings.MEDIA_ROOT, settings.DATABASES['default']['NAME'])) # Ejecutar el script en bash.
    os.chdir(a) # Cambiarse al directorio raíz del proyecto.
    messages = ['¡Se insertó la data .csv correctamente!']
    return render_to_response('registro/buscar.html', {'messages': messages}, context_instance=RequestContext(request))

def delete_csv(request):
    """
    @method delete_csv
    @brief Elimina todos los archivos .csv de la carpeta MEDIA_ROOT del proyecto.
    @param request
    @return Mensaje y redirección a template.
    @author Ing. Argenis Osorio <aosorio@cenditel.gob.ve>
    """
    # Almacena el directorio de trabajo actual para restaurarlo posteriormente.
    a = os.getcwd()

    # Ejecuta script bash que realiza la eliminación, pasando como parámetros:
    os.system("bash delete_csv.sh %s %s" % (settings.MEDIA_ROOT, settings.DATABASES['default']['NAME']))

    # Restaura el directorio de trabajo original.
    os.chdir(a)

    # Retorna mensaje de éxito.
    messages = ['¡Se eliminaron los archivos .csv correctamente!']

    return render_to_response('registro/buscar.html', {'messages': messages}, context_instance=RequestContext(request))

def formato_fecha(request):
    """
    Función que cambia el formato de hora y fecha de python
    """
    uploaded_at = datetime.now()
    fecha_hora = uploaded_at.strftime("%d-%m-%Y %H:%M")
    return render('registro/lista_certificados.html', {'uploaded_at': fecha_hora})


class Guardar_Certificado(SuccessMessageMixin, CreateView):
    """
    Clase que permite guardar los certificados, se guardar en /media.
    """
    model = Certificado
    form_class = CertificadoForm
    template_name = "registro/guardar_certificado.html"
    success_url = reverse_lazy('registro:buscar')
    success_message = "Se guardó el certificado con éxito"


class Lista_Certificados(ListView):
    """
    Clase que permite listar los certificados registrados.
    """
    model = Certificado
    #queryset = Certificado.objects.order_by('-uploaded_at')
    template_name = "registro/lista_certificados.html"


class Editar_Certificado(SuccessMessageMixin, UpdateView):
    """
    Clase que permite editar los certificados registrados.
    """
    template_name = "registro/editar_certificado.html"
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

        # Agrupar los certificados por los campos que definen la unicidad y
        # encontrar el id del registro más reciente en cada grupo.
        certificados_unicos = Certificado.objects.filter(cedula=q).values(
            'nombre_completo',
            'evento_curso',
            'rol'
        ).annotate(max_id=Max('id'))

        # Extraer los IDs de los registros más recientes.
        ids_unicos = [c['max_id'] for c in certificados_unicos]

        # Obtener los objetos completos usando los IDs únicos.
        certificados = Certificado.objects.filter(id__in=ids_unicos).order_by('-uploaded_at')

        if certificados:
            return render(request, 'registro/buscar.html', {'certificados': certificados, 'query': q})
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
