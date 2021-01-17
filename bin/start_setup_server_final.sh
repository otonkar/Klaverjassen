#!/bin/bash  

###
 # Script for installing NON-DOCKERIZED klaverjas app.
 #
 #  !! make sure the new server address is added to the NAS firewall is to allow connection
 #
 # Script to be run on the local host (ubuntu machine).
 # This script must be run from the klaverjassen/bin folder
 # This script will do the following
 #
 #   - Create an ssh key for root to log in from this local machine to the server without password
 #   - Copy scripts to install to the server
 #
 # SSH with root, to avoid the need to enter a password when a sudo command is given.
 #
 # Note: 
 #  * use ' ' when there need to be NO interpretation of the string
 #  * use "  " when the string parts must be interpretated, like: "./$INSTALL_GIT"
 #
###

### Variables
SERVER='95.216.159.105'
BRANCH='dev_005'
NAS='145.53.40.4'
INSTALL_GIT='install_local_git.sh'
INSTALL_PACKAGES='install_local_services.sh'

#####################################################################################
#### Create a sudo priveledged user on the remote server
#### https://www.digitalocean.com/community/tutorials/how-to-add-and-delete-users-on-ubuntu-18-04
echo "  "
echo "***** Create user ole on remote server"
echo "  "
ssh root@$SERVER "adduser ole && \
                  usermod -aG sudo ole \
                 "


#####################################################################################
#### Create ssh key to login from local machine to remote server without using password
echo "  "
echo "***** Create SSH keys for root"
echo "  "
mkdir -p ~/.ssh
ssh-keygen -t rsa

### Copy the public key to the remote host for root and user ole
# -o IdentitiesOnly for avoiding "Too many authentication failures"
ssh-copy-id -i $HOME/.ssh/id_rsa.pub -o IdentitiesOnly=yes  root@$SERVER
ssh-copy-id -i $HOME/.ssh/id_rsa.pub -o IdentitiesOnly=yes  ole@$SERVER
#ssh-copy-id -i ~/.ssh/id_rsa.pub 78.47.123.131    # This is for the current user on local machine (like ole)

#####################################################################################
#### Set the Ubuntu firewall 
#### Allow ssh and database connection for home location
#### Allow communication from port 80, 443 and 5000 from any location
ssh -t root@$SERVER " sudo ufw default deny incoming && \
                  sudo ufw default allow outgoing && \
                  sudo ufw allow from 145.53.40.4 to any port 22 proto tcp && \
                  sudo ufw allow 80,443,5000/tcp && \
                  sudo ufw enable \
                  "


# Do this manally
#####################################################################################
#### Create a key on remote server and share is to the NAS, so that 
#### the remote server an do rsync uploads to the NAS
##### !! NOTE the following does not work on a non admin, because only admin(NAS) can ssh(-copy-id) into the NAS
# ssh root@$SERVER "mkdir -p ~/.ssh && ssh-keygen -t rsa"

## ssh-copy-id does not seem to work within a ssh command
##     ssh root@$SERVER "ssh-copy-id -i $HOME/.ssh/id_rsa.pub admin@$NAS
## Therefore write the key manually to the NAS
##!!! does not work when doen remotely. Need to be done from terminal on the remote server
# ssh root@$SERVER "cat ~/.ssh/id_rsa.pub | ssh admin@$NAS 'umask 0077; mkdir -p .ssh; cat >> .ssh/authorized_keys' "


#####################################################################################
#### Copy the scripts to the remote machine
ssh root@$SERVER "mkdir -p /mybin"
rsync -rvz $INSTALL_GIT root@$SERVER:/mybin/
rsync -rvz $INSTALL_PACKAGES root@$SERVER:/mybin/


### next use root ssh (without password) to run the script remotely for install Git and aliases
echo "  "
echo "***** Setup GIT and aliases on the remote server"
echo "  "
ssh -t root@$SERVER "pwd && cd /mybin && chmod +x *.sh && ./$INSTALL_GIT"


#####################################################################################
### Get the klaverjassen code from the Github
echo "  "
echo "***** Git clone Klaverjassen"
echo "  "
ssh root@$SERVER "mkdir -p /code && cd /code && git clone https://github.com/otonkar/Klaverjassen.git"
ssh root@$SERVER "cd /code/Klaverjassen && git checkout "$BRANCH 


#####################################################################################
### Copy production.env from the local machine. set rw only for root
### Note: production.env needs to stay on the remote server in case Daphne needs to be started again
rsync -rvz ~/Programming/Git/Klaverjassen/production.env root@$SERVER:/code/Klaverjassen/production.env
ssh root@$SERVER "chmod 700 /code/Klaverjassen/production.env"

#####################################################################################
echo "  "
echo "***** Copy DB backup to mybin"
echo "  "
rsync -rvz $HOME/TMP/backup.dump root@$SERVER:/mybin/backup.dump


#####################################################################################
#### Install all the packages on the remote server
echo "  "
echo "***** Start installing packages......"
echo "  "
ssh -t root@$SERVER "cd /mybin && chmod +x *.sh && ./$INSTALL_PACKAGES"


################################
###############################
rsync -rvz test.sh root@$SERVER:/mybin/
ssh -t root@$SERVER "cd /mybin && chmod +x *.sh && ./test.sh"


