#!/bin/bash  

###
 # Script to be run on the remote production server for Klaverjassen.
 # The Klaverjas app should be cloned to /code
 # 
 # This script will create the docker images
 #
 # This script will be located in /code/Klaverjassen/bin/create_images.sh
###


#####################################################################################
### Load the production environment variables
source /code/Klaverjassen/production.env


#####################################################################################
### Create folders (/code is already created)
echo "  "
echo "***** Create folders"
echo "  "
mkdir -p /data/psql
mkdir -p /data/backup


# Set backend to read/write for everybody
# and create log folder
mkdir -p /code/Klaverjassen//backend/log
cd /code/Klaverjassen//backend
chmod -R 777 *
mkdir -p /code/Klaverjassen//backend/log

### Create the django base image
cd /code/Klaverjassen//backend
docker build -t django-base -f Dockerfile_django_base .


# In case this is a first start of the database, create a clean folder
rm -R /code/Klaverjassen/psql-data 
mkdir -p /code/Klaverjassen/psql-data 

# Next start the docker-compose
# Use the run_daphne_prd with the migrations on and create the base tables
cd /code/Klaverjassen
docker-compose -f docker-compose_prd.yml up --build