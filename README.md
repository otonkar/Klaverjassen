# Klaverjassen

This repository contains the code for the klaverjassen game.
It contains two parts:

* Backend: Django Restframework with Channels
* Frontend: Vue

## Django backend
The django and libraries can be installed using the 'install_backend.sh' script which is in the backend folder. First make this script executable and run the scipt.
This will create a virtual environment venv1, install the Django libraries, do the migrations and set some data in the tables.

```console
chmod 755 install_backend.sh
./install_backend.sh
source venv1/bin/activate
```

The backend consists of Django Restframework and a Redis server.
For development these can be started using

```console
python manage.py runserver 0.0.0.0:8000
docker run -p 6379:6379 -d redis:5
```

## Vue frontend
To build a frontend on another system do the following
* first clone this repo to the local machine. 
    * create folder ../Klaverjassen and do cd Klaverjassen
    * run git init
    * git remote add origin https://github.com/otonkar/Klaverjassen.git
    * git push -u origin master
* Now create the Vue project (overwrite modus)


```console
# goto folder ../Klaverjas
vue create frontend
# set options manually: Babel, Router, Vuex, CSS preprocesor, Linter
# Use history mode, dart SASS, ESlint with prevention only, in dedicated config files, npm

# Next install the libraries
cd frontend
vue add bootstrap-vue                       # use babel/polyfil
npm install --save reconnecting-websocket
npm install --save axios
npm i jquery@1.9.1 --save
npm audit fix --force 

# Next run the service
npm run serve
```

