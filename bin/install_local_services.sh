#!/bin/bash  

###
 # Script for installing NON-DOCKERIZED klaverjas app.
 #
 # This script installs the services for the klaverjas app
 #
 # SSH with root, to avoid the need to enter a password when a sudo command is given.
 #
###

#################################################################################
###### Set environment variables
echo "  "
echo "**** Set environment variables ****"
echo "  "
cd /code/Klaverjassen
source ./production.env


#################################################################################
###### Install Update and Upgrade
echo "  "
echo "**** Update and Upgrade ****"
echo "  "
sudo apt update
sudo apt upgrade


#################################################################################
###### Install Python libraries
###### Note: python3 is already installed
echo "  "
echo "**** Install Python packages ****"
echo "  "

## check version 
echo "Current python version: "
python3 -V

## install pip
sudo apt install python3-pip
sudo python3 -m pip install --upgrade pip

## Install needed libraries
sudo apt install python3-dev
sudo apt install gcc
sudo pip install psycopg2-binary

## pip install django libraries
cd /code/Klaverjassen/backend
sudo pip install -r ./requirements.txt


#################################################################################
###### Install Postgres db + restore DB backup
echo "  "
echo "**** Install Postgress and restore data ****"
echo "  "

## install postgress
sudo apt install postgresql postgresql-contrib

### Switch to postgres user and change password of default user postgress
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD '"$DB_PASSWORD"';"
echo "XXXXXXXXXXXXXXXXXX"

### Create the name of the database
sudo -u postgres createdb db_klaverjas

### Restore the DB backup
### note: this was copied to /mybin
cd /mybin
sudo chmod 777 backup.dump

### restore backup usin the postgres user
sudo -u postgres psql -U postgres db_klaverjas < backup.dump



