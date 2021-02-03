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
SERVER='168.119.60.235'
BRANCH='dev_006'
NAS='145.53.40.4'

#####################################################################################
#### Create ssh key to login from local machine to remote server without using password
echo "  "
echo "***** Create SSH keys for root"
echo "  "
mkdir -p ~/.ssh
ssh-keygen -t rsa

### Copy the public key to the remote host for root
# -o IdentitiesOnly for avoiding "Too many authentication failures"
ssh-copy-id -i $HOME/.ssh/id_rsa.pub -o IdentitiesOnly=yes  root@$SERVER
# ssh-copy-id -p 44933 -i $HOME/.ssh/id_ed25519 -o IdentitiesOnly=yes  ole@$SERVER
#ssh-copy-id -i ~/.ssh/id_rsa.pub 78.47.123.131    # This is for the current user on local machine (like ole)


#####################################################################################
#### Create a key on remote server and share is to the NAS, so that 
#### the remote server an do rsync uploads to the NAS
##### !! NOTE the following does not work on a non admin, because only admin(NAS) can ssh(-copy-id) into the NAS
ssh root@$SERVER "mkdir -p ~/.ssh && ssh-keygen -t rsa"

# ssh-copy-id does not seem to work within a ssh command
#     ssh root@$SERVER "ssh-copy-id -i $HOME/.ssh/id_rsa.pub admin@$NAS
# Therefore write the key manually to the NAS
ssh root@$SERVER "cat ~/.ssh/id_rsa.pub | ssh admin@$NAS 'umask 0077; mkdir -p .ssh; cat >> .ssh/authorized_keys' "


#####################################################################################
#### Copy the setup_server script to the remote machine
#### and run the script to install Git, docker, docker-compose and set aliases
# Next copy the installation files to the server
ssh root@$SERVER "mkdir -p /mybin"
rsync -rvz setup_server.sh root@$SERVER:/mybin/

### next use root ssh (without password) to run the script remotely for install and aliases
echo "  "
echo "***** Setup the remote server"
echo "  "
ssh root@$SERVER "pwd && cd /mybin && chmod +x * && ./setup_server.sh"


#####################################################################################
### Get the klaverjassen code from the Github
echo "  "
echo "***** Git clone Klaverjassen"
echo "  "
ssh root@$SERVER "mkdir -p /code && cd /code && git clone https://github.com/otonkar/Klaverjassen.git"
ssh root@$SERVER "cd /code/Klaverjassen && git checkout "$BRANCH 


#####################################################################################
### Set all the folders and create all the images and environments
echo "  "
echo "***** Create environments"
echo "  "
ssh root@$SERVER "chmod +x /code/Klaverjassen/bin/*.sh"
ssh root@$SERVER "/code/Klaverjassen/bin/create_images.sh"

#####################################################################################
### Copy production.env from the local machine
rsync -rvz ~/Programming/Git/Klaverjassen/production.env root@$SERVER:/code/Klaverjassen/production.env