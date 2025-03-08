#!/bin/bash

cd /var/www/hello-world-flask-app

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

sudo systemctl restart hello-world-flask-app.service