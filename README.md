# Repositorio que permite subir certificados digitales a un servidor y luego listarlos para descargarlos.

Creado por dM

## Versiones
```
Django==1.8.8
Python==2.7
```

## Dato

La base de datos es sqlite3, al
migrar se creara, así como
creara la tabla y campos descritos
en el modelo.

## Comandos para probar el proyecto

$ python manage.py makemigrations registro

$ python manage.py migrate

$ python manage.py runserver

## Importar la data desde el .csv

$ sqlite3 db.sqlite3

sqlite> .tables

sqlite> .mode csv

sqlite> .import data.csv registro_certificado

sqlite> .exit
