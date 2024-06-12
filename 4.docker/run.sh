#!/bin/bash

docker run -d -p 8000:8000 -it web python manage.py runserver 0.0.0.0:8000

# docker compose up --build -d