#!/bin/sh
###
 # Script to start the Daphne application in development.
###

# Make sure when an error occurs to exit the script with an error.
# After the error the other commands will not be executed.
set -e

# load the enviroment variables (defined as: export ENV="development")
source ../backend_dev.env

# Run the migrations
# python manage.py makemigrations my_auth
# python manage.py makemigrations klaverjas
# python manage.py makemigrations appwebsocket
# python manage.py makemigrations
# python manage.py migrate

# start the daphne server for the backend on port 6000 within the container
daphne -b 0.0.0.0 -p 6000 back1.asgi:application