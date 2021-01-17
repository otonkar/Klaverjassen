#!/bin/bash  

###
 # Script for installing NON-DOCKERIZED klaverjas app.
 #
 # This script installs the services for the klaverjas app
 #
 # SSH with root, to avoid the need to enter a password when a sudo command is given.
 #
###

NAS_HOST='145.53.40.4'

#################################################################################
###### Set environment variables
echo "  "
echo "**** Set environment variables ****"
echo "  "
cd /code/Klaverjassen
source ./production.env


#################################################################################
###### Install Update and Upgrade
echo "  "
echo "**** Update and Upgrade ****"
echo "  "
sudo apt update
sudo apt upgrade


#################################################################################
###### Install Python libraries
###### Note: python3 is already installed
echo "  "
echo "**** Install Python packages ****"
echo "  "

## check version 
echo "Current python version: "
python3 -V

## install pip
sudo apt install python3-pip
sudo python3 -m pip install --upgrade pip

## Install needed libraries
sudo apt install python3-dev
sudo apt install gcc
sudo pip install psycopg2-binary

## pip install django libraries
cd /code/Klaverjassen/backend
sudo pip install -r ./requirements.txt


#################################################################################
###### Install Postgres db + restore DB backup
echo "  "
echo "**** Install Postgress and restore data ****"
echo "  "

## install postgress
sudo apt install postgresql postgresql-contrib

### Switch to postgres user and change password of default user postgress
sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD '"$DB_PASSWORD"';"
echo "XXXXXXXXXXXXXXXXXX"

### Create the name of the database
sudo -u postgres createdb db_klaverjas

### Restore the DB backup
### note: this was copied to /mybin
cd /mybin
sudo chmod 777 backup.dump

### restore backup usin the postgres user
sudo -u postgres psql -U postgres db_klaverjas < backup.dump


#################################################################################
echo "  "
echo "**** Install Redis ****"
echo "  "
sudo apt install redis-server
## in /etc/redis/redis.conf   set 'supervised no' to 'supervised systemd'
sudo sed -i '/supervised no/c\supervised systemd' /etc/redis/redis.conf


#################################################################################
echo "  "
echo "**** Install Nodejs and NPM  ****"
echo "  "
sudo apt install nodejs
sudo apt install npm
## check version
echo "nodejs version: "
nodejs -v
echo "npm version :"
npm --version


#################################################################################
echo "  "
echo "**** Build Vue frontend  ****"
echo "  "
cd /code/Klaverjassen/frontend/project
npm install
npm audit fix
# Create dist folder with production frontend.
npm run build
## Make sure that when Nginx is installed that the dist folder is move to the correct location
sudo mkdir -p /var/www/klaverjasfun
sudo cp -R /code/Klaverjassen/frontend/project/dist /var/www/klaverjasfun


#################################################################################
echo "  "
echo "**** Install Nginx  ****"
echo "  "
sudo apt install nginx

### Copy the default page to /var/www/html and remove the current page
cp /code/Klaverjassen/frontend/nginx/maintenance.html /var/www/html/index.html
rm /var/www/html/index.nginx-debian.html

### Fist copy the temporary conf file to the klaverjasdomain.
### This file does not contain any Certbot settings, so this can be used when a certificate is generated
sudo cp /code/Klaverjassen/frontend/nginx/conf.d/klaverjasfun_tmp /etc/nginx/sites-available/klaverjasfun
## Enable the klaverjasfun domain by creating a symlink to sites-enabled
sudo ln -s /etc/nginx/sites-available/klaverjasfun /etc/nginx/sites-enabled/

### Install Certbot for SSL
sudo apt install certbot python3-certbot-nginx
### get certificate
### do this before the domains are added, so that the conf file for klaverjasfun can be re-used
sudo certbot --nginx -d klaverjasfun.nl -d klaverjasfun.nl

### The settings for klaverjasfun have now been updated by Certbot.
### This update will be stored on other place and we place back out settings file
sudo cp /etc/nginx/sites-available/klaverjasfun /mybin/klaverjasfun_updated


## Copy klaverjasfun nginx settings to sites-availabled
sudo cp /code/Klaverjassen/frontend/nginx/conf.d/klaverjasfun /etc/nginx/sites-available/klaverjasfun
## Enable the klaverjasfun domain by creating a symlink to sites-enabled (not needed because link is already created)
# sudo ln -s /etc/nginx/sites-available/klaverjasfun /etc/nginx/sites-enabled/


## Check errors in nginx config and reload
sudo nginx -t
sudo systemctl reload nginx


#################################################################################
echo "  "
echo "**** Install supervisor  ****"
echo "  "
sudo apt install supervisor
### copy the settings to the supervisor folder
cp /code/Klaverjassen/bin/supervisord.conf /etc/supervisor/conf.d/supervisord.conf


##@@@@@  Add supervisor start


#################################################################################
echo "  "
echo "**** Set DB backup script  ****"
echo 
### create the backup folder
sudo mkdir -p /var/backups/psql
sudo chmod 777 /var/backups/psql
### Copy the backup script to the backup folder
sudo cp /code/Klaverjassen/bin/backup_psql_daily.sh /var/backups/psql
sudo chmod +x *.sh

### Create the crontab 
sudo crontab -l | { cat; echo '20 2 * * *  /var/backups/psql/backup_psql_daily.sh'; } | crontab -
sudo crontab -l | { cat; echo '25 2 * * 0 rsync -rvz /var/backups/psql/$(ls -t /var/backups/psql |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_0.dump"; } | crontab -
sudo crontab -l | { cat; echo '25 2 * * 1 rsync -rvz /var/backups/psql/$(ls -t /var/backups/psql |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_1.dump"; } | crontab -
sudo crontab -l | { cat; echo '25 2 * * 2 rsync -rvz /var/backups/psql/$(ls -t /var/backups/psql |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_2.dump"; } | crontab -
sudo crontab -l | { cat; echo '25 2 * * 3 rsync -rvz /var/backups/psql/$(ls -t /var/backups/psql |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_3.dump"; } | crontab -
sudo crontab -l | { cat; echo '25 2 * * 4 rsync -rvz /var/backups/psql/$(ls -t /var/backups/psql |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_4.dump"; } | crontab -
sudo crontab -l | { cat; echo '25 2 * * 5 rsync -rvz /var/backups/psql/$(ls -t /var/backups/psql |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_5.dump"; } | crontab -
sudo crontab -l | { cat; echo '25 2 * * 6 rsync -rvz /var/backups/psql/$(ls -t /var/backups/psql |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_6.dump"; } | crontab -




#################################################################################
echo "  "
echo "**** Create log file  ****"
echo "  "
mkdir -p /code/Klaverjassen/backend/log
sudo touch /code/Klaverjassen/backend/log/auth.log
sudo touch /code/Klaverjassen/backend/log/debug.log
sudo touch /code/Klaverjassen/backend/log/default.log
sudo touch /code/Klaverjassen/backend/log/errors.log
sudo touch /code/Klaverjassen/backend/log/registration.log
sudo touch /code/Klaverjassen/backend/log/root.log



