#!/bin/bash  

###
 # Script to set the correct settings and install the programs
 # that are needed on a Ubuntu 18.04 server to be used for the klaverjassen app
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

# Make sure ole can run docker without sudo
sudo groupadd docker
sudo usermod -aG docker ole
# sudo usermod -aG docker $USER

#################################################################################
###### Install docker-compose
echo "  "
echo "**** Install docker-compose ****"
echo "  "
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

#################################################################################
###### Install Git
echo "  "
echo "**** Install Git ****"
echo "  "
sudo apt update
sudo apt install git

#################################################################################
###### Clean up
sudo apt autoremove

#################################################################################
###### Create .bash_aliases
FILE="/root/.bash_aliases"

/bin/cat <<EOM >$FILE
### General aliases
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
alias diruse='sudo du -hx --max-depth=1 |sort -hr'        ## show format 325M of 125K
alias cpu='cat /proc/cpuinfo | grep "MHz"'
alias h="history | tail -n 1000 | tac | more"
alias pa="ps aux|more"

# GIT
alias gpom="git push origin master"
alias gb="git branch"
alias gco="git checkout"
alias gs="git status"
alias ga="git add ."
alias gc="git commit -m "
alias gp="git push"


### Nginx
alias nginx_stop='sudo systemctl stop nginx'
alias nginx_start='sudo systemctl start nginx'
alias nginx_restart='sudo systemctl restart nginx'
alias nginx_reload='sudo systemctl reload nginx'
EOM

cp /root/bash_aliases /home/ole/.bash_aliases


