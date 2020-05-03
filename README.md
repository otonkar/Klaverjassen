# Klaverjassen

This repository contains the code for the klaverjassen game.
It contains two parts

* Backend: Django Restframework with Channels
* Frontend: Vue

## Django backend
The django and libraries can be installed using the 'install_backend.sh' script.
First make this script executable and run the scipt.
This will create a virtual environment venv1 and install the Django libraries

```console
chmod 755 install_backend.sh
./install_backend.sh
source venv1/bin/activate
```

The backend consists of Django Restframework and a Redis server.
These can be started using

```console
python manage.py run server 0.0.0.0:8000
docker run -p 6379:6379 -d redis:5
```

## Vue frontend
To build a frontend on another system do the following
* first clone this repo to the local machine. 
    * create folder ../Klaverjassen and do cd Klaverjassen
    * run git init
    * git remote add origin https://github.com/otonkar/Klaverjassen.git
    * git push -u origin master
* Next copy the Klaverjas/frontend/src folder to a temporary location
* Remove the /Klaverjas/frontend folder (rm -R frontend)
* Now create the Vue project 


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

# Next remove newly create src
cd frontend
rm -R src
```

* Next copy back the ./src folder

