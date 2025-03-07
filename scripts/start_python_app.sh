#!/bin/bash

cd /home/ec2-user/hello-world-python-app

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

sudo systemctl resrart hello-world-python-app.service