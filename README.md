# Repositorio que permite subir certificados digitales a un servidor y luego listarlos para descargarlos.

Desarrollado por Ing. Argenis Osorio

*Paquetes del sistema operativo requeridos:

sqlite3

*Paquetes de Python requeridos: 

Django 1.8.8
Python 2.7

## Instalar el proyecto en un entorno de desarrollo:

Nota:
Usaremos $ para describir los comandos que se usaran con usuario regular.
Usaremos # para describir los comandos que se usaran con superusuario. 

1) Instalar los siguientes paquetes para crear entornos virtuales

# apt-get install install python-setuptools python-dev

# apt-get install python-virtualenv virtualenvwrapper

2) Crear un entorno virtual de python

$ virtualenv mi_env

$ source mi_env/bin/activate

3) Instalación de requerimientos del proyecto

$ pip install -r repositorio_certificados/requirements.txt 

4) Probar el proyecto

$ cd repositorio_certificados

$ cp repositorio_certificados/settings.py_example repositorio_certificados/settings.py

$ python manage.py makemigrations registro

$ python manage.py migrate

$ python manage.py createsuperuser

$ python manage.py runserver

----

# Importar datos en la base de datos desde un .csv

$ sqlite3 db.sqlite3

sqlite> .tables

sqlite> .mode csv

sqlite> .import data.csv registro_certificado

sqlite> .exit

----

##  Pasos a seguir para subir certificados al repositorio

1) Subir un archivo .zip que contenga los certificados desde el formulario disponible desde /subir_data, el .zip
debe contener una carpeta con el nombre del evento y dentro deben estar los certificados.

2) Descomprimir y borrar el fichero .zip con la opción "Descomprimir .zip y  borrar .zip"

3) Subir el archivo data_final.csv desde el formulario disponible desde /subir_data_csv

4) Insertar la data en la base de datos con la opción "Insertar data .csv"