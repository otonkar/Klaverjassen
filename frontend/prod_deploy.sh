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
#
# this script is run from   ../Klaverjassen/frontend
#
# Redis, Daphne and Postgress must be started separately


# Set the environment variables for PRODUCTION
export VUE_APP_URL_API_BASE='https://klaverjasfun.nl:5000/'
export VUE_APP_URL_WEBSOCKET='wss:klaverjasfun.nl:5000/ws/game/'

# build the frontend
cd /apps/Klaverjassen/frontend/project
rm -R dist
npm run build
nginx_restart

# Set the Django settings.py
cd /apps/Klaverjassen/backend/back1/back1
rm settings.py
ln -s settings_prod.py settings.py