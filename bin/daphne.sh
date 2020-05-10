#!/bin/bash
# Script to start daphne service

# Start virtual environment
cd /apps/backend
source venv1/bin/activate

cd back1
daphne -p 6000 back1.asgi:application

