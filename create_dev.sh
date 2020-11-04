#!/bin/bash  

###
 # Bash file to create the base image and 
 # and start the development backend
###

# Make sure the postgres data folder exists.
mkdir -p psql-data

# first remove all containers
docker container prune

# Create the base image
# Once ceated this only needs to be rebuilt when the virtual environment changes
cd backend
docker build -t django-base -f Dockerfile_django_base .

# start the containers, do not used detached mode -d
# so that
cd ..
docker-compose -f docker-compose_backend_dev.yml up --build



