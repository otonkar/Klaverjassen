This is an example on how to dockerize full app using
 - Vue frontend
 - Django backend
 - nginx poxy / webserver

The basic setup is a described in the tutorial below:
https://www.youtube.com/watch?v=nh1ynJGJuT8
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

The main folder will contain the following folders
 - frontend   : the source files for the frontend
 - backend    : the source files for the backend
 - nginx      : the configuration files for the proxy
 - scripts    : general scripts to support the deployment and setup


Guidelines:
 - Every service should have its own folder, with its own environment files
 - The Dockerfiles are in the root folders of the service (like backend folder)
 - The docker-compose files are in the higest level folder, because the docker-compose
   will need to setup all the services in a docker network
 - Each service can have its own scripts folder that are specific for that service

**** Backend setup ****
The folder structure for the Django backend service is:

 - backend    (contains the requirements.txt)
  | - scripts (scripts specific for the backend)
  | - back1   (contains the Django manage.py)
    | - back1 (contains the settings.py)

Create the backend image from the backend folder
  docker build -t backend .
  docker build -f Dockerfile_backend -t backend .


To run this image in interactive mode do
  docker run -it --rm backend /bin/ash
  docker run -it --rm docker_full_app_app /bin/ash
  docker-compose -f docker-compose_backend_dev.yml run -p 7000:8000  app sh
 #







** First create a default Django app.
In the main folder do
make sure the venv1 environment is created outside the src folder.

--------
python3 -m venv venv1
source venv1/bin/activate
pip install django
pip freeze > requirements.txt

mkdir -p src
cd src

django-admin.py startproject hello_django .
python manage.py migrate
python manage.py runserver 0.0.0.0:5000
-------


docker build -t backend .
docker run -it --rm djangotest /bin/ash

