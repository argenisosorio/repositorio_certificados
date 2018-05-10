#!/bin/bash

rm -rf registro/migrations/

echo "Removidas migraciones del registro"

rm -rf db.sqlite3

echo "Removidas la base de datos"

python manage.py makemigrations registro

echo "Migrados los registros"

python manage.py migrate

echo "Creada la base de datos"

python manage.py createsuperuser

echo "Creado el superusuario"
