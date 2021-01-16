#!/bin/bash
# Script to start daphne service

# Set the enviroment variables. 
# Use sudo, because production.env is only to be read by root
cd /code/Klaverjassen
sudo source ./production.env

cd back1
daphne -p 6000 back1.asgi:application



#### Old setup
# # Start virtual environment
# cd /apps//Klaverjassen/backend
# source venv1/bin/activate

# cd back1
# daphne -p 6000 back1.asgi:application

