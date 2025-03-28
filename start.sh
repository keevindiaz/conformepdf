#!/bin/bash
pip install -r requirements.txt  # Instalación de dependencias de Python
gunicorn app:app  # Inicia la app Flask con gunicorn
