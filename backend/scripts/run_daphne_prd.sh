#!/bin/sh
###
 # Script to start the Django application in development.
###

# Make sure when an error occurs to exit the script with an error.
# After the error the other commands will not be executed.
set -e

######################################################################
#######  RUN THIS PART ONLY WHEN NO DATABASE HAS BEEN ALREADY CREATED

# echo "*** Do the database migrations"
# python manage.py makemigrations my_auth
# python manage.py migrate my_auth
# python manage.py makemigrations klaverjas
# python manage.py migrate klaverjas
# python manage.py makemigrations appwebsocket
# python manage.py migrate appwebsocket
# python manage.py makemigrations
# python manage.py migrate

# #####################################################################
# #### Only run the first time to set base tables in an empty database
# echo "*** Create superuser and test users"
# python manage.py runscript setup_create_users.py

# echo "*** Set the GameStatus tabel"
# python manage.py runscript setup_gameStatus.py

# echo "*** Set the Troef tabel"
# python manage.py runscript setup_troef.py

#######  END PART
#####################################################################

# start the daphne server for the backend on port 6000 within the container
daphne -b 0.0.0.0 -p 6000 back1.asgi:application
# python manage.py runserver 0.0.0.0:6000