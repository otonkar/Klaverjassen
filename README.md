# Klaverjassen

This repository contains the code for the klaverjassen game.
It contains two parts:

* Backend: Django Restframework with Channels
* Frontend: Vue

The procedure below describes how this repository can be downloaded to a local machine 
and how the backend and fronend can be installed

## Download repository
To download this repository to a folder folder/Klaverjassen do the following.
Clone this repository to the folder. This will create the subfolder Klaverjassen (repository name)
```console
git clone https://github.com/otonkar/Klaverjassen.git
```

Next set the respository to the branch you want to install.
For example: work from branch dev_001
```console
cd Klaverjassen
git checkout dev_001
```

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
The frontend is created using the 'install_frontend.sh script.
This script is in the ../Klaverjassen folder.
Make this script executable and run the script
```console
chmod 755 install_frontend.sh
./install_frontend.sh
```

This script will first copy the Vue source file to a tmp folder.
Next the npm installs will be done.
After that the source files are copied back into the Vue project.

In the script the Vue project is created using 'vue create' command.
Use the following settings to be provided manually
* manually set options
* Choose, Babel, Router, Vuex, CSS preprocesor, Linter
* Use history mode, dart SASS, ESlint with prevention only, in dedicated config files, npm

After the Vue project is installed start the Vue development server using:

```console
cd frontend
npm run serve
```

cd frontend
vue add bootstrap-vue                       # use babel/polyfil
npm install --save reconnecting-websocket
npm install --save axios
npm i jquery@1.9.1 --save
npm audit fix --force 
