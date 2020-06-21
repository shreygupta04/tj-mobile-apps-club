#!/bin/bash
source ../mobileapps/venv/bin/activate
gunicorn run:app -b 127.0.0.1:$PORT -w=1