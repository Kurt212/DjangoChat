#! /bin/sh

sudo docker run -p 6379:6379 -d redis:2.8

python3 ./manage.py makemigrations chat
python3 ./manage.py migrate

python3 ./manage.py runserver
