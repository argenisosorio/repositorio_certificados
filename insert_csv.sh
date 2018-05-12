#!/bin/sh
sqlite3 db.sqlite3 <<EOF
.mode csv
.import media/data_final.csv registro_certificado
EOF
rm -rf media/*.csv # Remover todos los .csv del directorio /media/