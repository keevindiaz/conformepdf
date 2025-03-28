#!/bin/bash
apt-get update && apt-get install -y wkhtmltopdf
gunicorn app:app
