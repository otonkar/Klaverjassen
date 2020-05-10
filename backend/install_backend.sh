#!/bin/bash 
#
# script to setup the Django backend
# First do chmod 777 install_backend
# Start this script in terminal from the /backend folder, ./install_backend

# When all django files are downloaded from the Github respository then 
# first copy all these files to a temporary folder
# Make sure that only requirements.txt is in the klaverjas folder
mv back1 tmp
# cp tmp/requirements.txt klaverjas/requirements.tx

### Create a virtual environment and install Django
VENV_NAME='venv1'

# Create the virtual environment and start this.
python3 -m venv $VENV_NAME
source $VENV_NAME/bin/activate

# Install the libraries
pip install -r requirements.txt
pip install daphne

### Create a django project back1
django-admin startproject back1

## copy all filesfrom tmp folder to klaverjas 
cp -R tmp/* back1/
rm -R tmp

## setup Django
cd back1
chmod 777 setup.sh
./setup.sh
