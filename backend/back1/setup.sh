#!/bin/bash 
#
# Setup file setting up the klaverjas backend
# This setup creates a couple of users and sets the database

echo "*** Setup of backend: back1"
echo " "

echo "First make sure the sqlite database is not present"
rm db.sqlite3

echo "*** Do the database migrations"
python manage.py makemigrations
python manage.py migrate

echo "*** Create superuser and test users"
python manage.py runscript setup_create_users.py

echo "*** Set the GameStatus tabel"
python manage.py runscript setup_gameStatus.py

echo "*** Set the Troef tabel"
python manage.py runscript setup_troef.py

