#!/bin/bash  

###
 # Script to be run on the remote production server for Klaverjassen.
 # The Klaverjas app should be cloned to /code
 # 
 # This script will create the docker images
 #
 # This script will be located in /code/Klaverjassen/bin/create_images.sh
###

### Load the production environment variables
source ../production.env

### Create the django base image
cd ../backend
docker build -t django-base -f Dockerfile_django_base .


