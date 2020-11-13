#!/bin/bash  

###
 # Script to be run on the remote production server for Klaverjassen.
 # The Klaverjas app should be cloned to /code
 # 
 # This script will create the docker images
 #
 # This script will be located in /code/Klaverjassen/bin/create_images.sh
###

# Variables
BASE_DIR='/code/Klaverjassen'

#####################################################################################
### Load the production environment variables
source $BASE_DIR/production.env


#####################################################################################
### Create folders (/code is already created)
echo "  "
echo "***** Create folders"
echo "  "
mkdir -p /data/psql
mkdir -p /data/backup
mkdir -p /data/nginx/log
mkdir -p /data/nginx/letsencrypt


# Set backend to read/write for everybody
# and create log folder
mkdir -p $BASE_DIR/backend/log
cd $BASE_DIR/backend
chmod -R 777 *


#####################################################################################
### ### Create the django base image
echo "  "
echo "***** Create Django base image"
echo "  "
cd $BASE_DIR/backend
docker build -t django-base -f Dockerfile_django_base .

#####################################################################################
### Create the Nginx image and start the services
###
### Use the run_daphne_prd with the migrations on and create the base tables
echo "  "
echo "***** Docker compose / create Nginx image"
echo "  "
cd $BASE_DIR
docker-compose -f docker-compose_prd.yml up --build


#####################################################################################
### Add a job to cron, that will run the daily backup in the postgres images
### Note: /data/backup of the server will be mouted to /tmp in the postgres image
### Ensure to add an empty line ??
cp ./backup_psql_daily.sh /data/backup/backup_psql_daily.sh
crontab -l | { cat; echo "*/5 * * * * docker exec -t klaverjas_psql_prd /tmp/backup_psql_daily.sh"; } | crontab -
crontab -l | { cat; echo "#"; } | crontab -