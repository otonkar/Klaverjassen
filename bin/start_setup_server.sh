#!/bin/bash  

###
 # Script to be run on the local host (ubuntu machine).
 # This script must be run from the klaverjassen/bin folder
 # This script will do the following
 #
 #   - Create an ssh key for root to log in from this local machine to the server without password
 #   - Copy scripts to install to the server
 #
###

### Variables
SERVER='78.47.123.131'
BRANCH='dev_004'

#####################################################################################
### Create ssh key and install docker, docker compose and git, and aliases

# ### Create a ssh key on for this local machine to log in as root
# echo "  "
# echo "***** Create SSH keys for root"
# echo "  "
# mkdir -p ~/.ssh
# ssh-keygen -t rsa

# ### Copy the public key to the remote host for root
# ssh-copy-id -i $HOME/.ssh/id_rsa.pub root@$SERVER
# #ssh-copy-id -i ~/.ssh/id_rsa.pub 78.47.123.131    # This is for the current user (like ole)

# #### Copy the setup_server script to the remote machine
# # Next copy the installation files to the server
# rsync -rvz setup_server.sh root@$SERVER:/mybin/

# ### next use root ssh (without password) to run the script remotely for install and aliases
# echo "  "
# echo "***** Setup the remote server"
# echo "  "
# ssh root@$SERVER "pwd && cd /mybin && chmod +x * && ./setup_server.sh"


#####################################################################################
### Create a /code folder and git clone klaverjassen
echo "  "
echo "***** Git clone Klaverjassen"
echo "  "
ssh root@$SERVER "mkdir -p /code && cd /code && git clone https://github.com/otonkar/Klaverjassen.git"
ssh root@$SERVER "cd /code/Klaverjassen && git checkout "$BRANCH 

#####################################################################################
### Create the images
echo "  "
echo "***** Create base images"
echo "  "
ssh root@$SERVER "cd chmod =x /code/Klaverjassen/bin/*.sh"
ssh root@$SERVER "cd /code/Klaverjassen/bin/create_images.sh"