# Repositorio que permite subir certificados digitales a un servidor y luego listarlos para descargarlos.

Creado por dM

## Paquetes requeridos

De GNU/Linux Debian
```
sqlite3
```

De Python
```
Django==1.8.8
Python==2.7
```

## Instalación de paquetes para crear entornos virtuales
```
# apt-get install install python-setuptools python-dev

# apt-get install python-virtualenv virtualenvwrapper
```
## Crear un entorno virtual de python
```
$ virtualenv mi_env

$ source mi_env/bin/activate
```
## Instalación de requerimientos del proyecto
```
$ pip install -r repositorio_certificados/requirements.txt 
```
## Probar el proyecto
```
$ cd repositorio_certificados

$ cp repositorio_certificados/settings.py_example repositorio_certificados/settings.py

$ python manage.py makemigrations registro

$ python manage.py migrate

$ python manage.py createsuperuser

$ python manage.py runserver
```
## Importar la data en la base de datos desde un .csv
```
$ sqlite3 db.sqlite3

sqlite> .tables

sqlite> .mode csv

sqlite> .import data.csv registro_certificado

sqlite> .exit
```
