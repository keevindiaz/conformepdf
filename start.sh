#!/bin/bash

chmod +x bin/wkhtmltopdf
gunicorn app:app
