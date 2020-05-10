#!/bin/bash 
#
# script to setup the Vue frontend
# This script is in the main folder Klaverjassen
# First make this script executable
#     chmod 777 install_frontend

# Start this script in terminal from the /Klaverjassen folder and do:  ./install_frontend

# First move the frontend file to a tmp folder
mv project tmp

# Next create the Vue frontend
echo "*** Create vue project "
vue create project

# and do the other installs
echo " "
echo "*** Install bootstrap-vue, reconnecting websocket and axios"
cd project
#npm install
vue add bootstrap-vue                       # use babel/polyfil Y
npm install --save reconnecting-websocket
npm install --save axios
npm i jquery@1.9.1 --save
npm audit fix --force 


## Go back the Klaverjassen folder copy back the files from tmp
cd ..
cp -R tmp/* project
rm -R tmp







