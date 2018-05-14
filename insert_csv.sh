#!/bin/sh
MEDIA=$1
DB=$2
#sqlite3 db.sqlite3 <<EOF
#.import media/data_final.csv registro_certificado
sqlite3 $DB <<EOF
.mode csv
.import $MEDIA/data_final.csv registro_certificado
EOF
#rm -rf media/*.csv # Remover todos los .csv del directorio /media/
rm -rf $MEDIA/*.csv # Remover todos los .csv del directorio /media/