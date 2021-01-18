#!/bin/bash
# Script to start daphne service

# Set the enviroment variables. 
# run as root
source /code/Klaverjassen/production.env

cd /code/Klaverjassen/backend/back1
daphne -p 6000 back1.asgi:application



