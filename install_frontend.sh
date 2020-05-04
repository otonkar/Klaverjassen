#!/bin/bash 
#
# script to setup the Vue frontend
# This script is in the main folder Klaverjassen
# First do chmod 777 install_frontend
# Start this script in terminal from the /frontend folder, ./install_frontend

# First move the frontend file to a tmp folder
mv frontend tmp

# Next create the Vue frontend


## copy all filesfrom tmp folder to klaverjas 
cp -R tmp/* back1/

## setup Django
cd back1
chmod 777 setup.sh
./setup.sh
