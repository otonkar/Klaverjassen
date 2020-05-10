#!/bin/bash 
#
# Setup file setting up the klaverjas backend
# This setup creates a couple of users and sets the database

export SECRET_KEY='j5!38#d%j38j(9=7wo%e5!@!##g%ti$%^7qgu)cuu+j*lh*ei2'

cd back1
rm settings.py
ln -s settings_dev.py settings.py
# cp settings_dev.py settings.py

echo "*** Setup of backend: back1"
echo " "

echo "First make sure the sqlite database is not present"
cd ..
3rm db.sqlite3

echo "*** Do the database migrations"
python3 manage.py makemigrations my_auth
python3 manage.py migrate my_auth
python3 manage.py makemigrations klaverjas
python3 manage.py migrate klaverjas
python3 manage.py makemigrations channels
python3 manage.py migrate channels
python3 manage.py makemigrations appwebsocket
python3 manage.py migrate appwebsocket
python3 manage.py makemigrations
python3 manage.py migrate


echo "*** Create superuser and test users"
python3 manage.py runscript setup_create_users.py

echo "*** Set the GameStatus tabel"
python3 manage.py runscript setup_gameStatus.py

echo "*** Set the Troef tabel"
python3 manage.py runscript setup_troef.py

