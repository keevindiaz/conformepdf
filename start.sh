#!/bin/bash

chmod +x ./bin/wkhtmltopdf   # << Esto agrega el permiso de ejecución EN RENDER
echo "Verificando permisos..."
ls -l ./bin/wkhtmltopdf
file ./bin/wkhtmltopdf

# Iniciar el servidor con gunicorn
gunicorn app:app --bind 0.0.0.0:10000
