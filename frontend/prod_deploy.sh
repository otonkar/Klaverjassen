#!/bin/bash 
#
# script deploy the new version of backend and frontend
#
# Starting point is that the correct git respository is active
#    git checkout prod_00x
#
# This script will do the following
#  * set the production environment variables
#  * build the fontend
#  * link settings_prod.py to the settings.py file
#  * copy bin files to the correct place
#
# this script is run from   ../Klaverjassen/frontend
#
# Redis, Daphne and Postgress must be started separately

# Go to Django folder and do the migrations
cd /apps/Klaverjassen/backend
source venv1/bin/activate
cd back1
python3 manage.py makemigrations
python3 manage.py migrate

deactivate

# Set the Django settings.py
cd /apps/Klaverjassen/backend/back1/back1
touch settings.py
rm settings.py
ln -s settings_prod.py settings.py

# Create folders if not exist
mkdir -p /apps/Klaverjassen/log/

# Set the environment variables for PRODUCTION
export VUE_APP_URL_API_BASE='https://klaverjasfun.nl:5000/'
export VUE_APP_URL_WEBSOCKET='wss:klaverjasfun.nl:5000/ws/game/'

# copy bin files to the correct place
cp /apps/Klaverjassen/bin/supervisord.conf /etc/supervisord.conf
cp /apps/Klaverjassen/bin/default_prod /etc/nginx/sites-available/default

# build the frontend
cd /apps/Klaverjassen/frontend/project
rm -R dist
npm run build

# reload and restart nginx
nginx_reload
nginx_restart

# Go back to folder in which the script was started
cd /apps/Klaverjassen/frontend