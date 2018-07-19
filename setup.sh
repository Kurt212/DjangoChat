#! /bin/sh

sudo apt-get install python3-pip
sudo pip3 install Django

pip3 install -U channels
pip3 install channels_redis

sudo docker run -p 6379:6379 -d redis:2.8

python3 ./manage.py makemigrations chat
python3 ./manage.py migrate

python3 ./manage.py runserver
