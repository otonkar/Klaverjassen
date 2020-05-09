#!/bin/bash 
#
# Setup file setting up the klaverjas backend
# This setup creates a couple of users and sets the database

export SECRET_KEY='j5!38#d%j38j(9=7wo%e5!@!##g%ti$%^7qgu)cuu+j*lh*ei2'

cd back1
cp settings_dev.py settings.py

echo "*** Setup of backend: back1"
echo " "

echo "First make sure the sqlite database is not present"
rm db.sqlite3

echo "*** Do the database migrations"
python manage.py makemigrations my_auth
python manage.py migrate my_auth
python manage.py makemigrations klaverjas
python manage.py migrate klaverjas
python manage.py makemigrations channels
python manage.py migrate channels
python manage.py makemigrations appwebsocket
python manage.py migrate appwebsocket

echo "*** Create superuser and test users"
python manage.py runscript setup_create_users.py

echo "*** Set the GameStatus tabel"
python manage.py runscript setup_gameStatus.py

echo "*** Set the Troef tabel"
python manage.py runscript setup_troef.py

