#!/bin/bash  

###
 # For installing the NON-DOCKERIZED services
 #
 # Script for installing GIT and settting aliases
 #
 # this script must be run as root
###

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
echo "  "
echo "**** Create aliases ****"
echo 

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

## only when user ole has been created on the server
cp /root/bash_aliases /home/ole/.bash_aliases




