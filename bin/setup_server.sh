#!/bin/bash  

###
 # Script to set the correct settings and install the programs
 # that are needs on a Ubuntu 18.04 server to be used for the klaverjassen app
 #
 # this script must be run as root
###

#################################################################################
###### Add user ole and add to the sudo rights
adduser ole
usermod -aG sudo ole

#################################################################################
###### Install Docker
echo "  "
echo "**** Install docker ****"
echo "  "
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
    
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
   
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io  

#################################################################################
###### Install docker-compose
echo "  "
echo "**** Install docker-compose ****"
echo "  "
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

#################################################################################
###### Install Git
echo "  "
echo "**** Install Git ****"
echo "  "
sudo apt update
sudo apt install git


