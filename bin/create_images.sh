#!/bin/bash  

###
 # Script to be run on the remote production server for Klaverjassen.
 # The Klaverjas app should be cloned to /code
 # 
 # This script will create the docker images
 #
 # This script will be located in /code/Klaverjassen/bin/create_images.sh
###

# Variables
BASE_DIR='/code/Klaverjassen'
NAS_HOST='145.53.40.4'
RSYNC_SCRIPT='/data/backup/rsync_script.sh'


#####################################################################################
### Load the production environment variables
source $BASE_DIR/production.env


#####################################################################################
### Create folders (/code is already created)
echo "  "
echo "***** Create folders"
echo "  "
mkdir -p /data/psql
mkdir -p /data/backup
mkdir -p /data/nginx/log
mkdir -p /data/nginx/letsencrypt


# Set backend to read/write for everybody
# and create log folder
mkdir -p $BASE_DIR/backend/log
cd $BASE_DIR/backend
chmod -R 777 *


#####################################################################################
### ### Create the django base image
echo "  "
echo "***** Create Django base image"
echo "  "
cd $BASE_DIR/backend
docker build -t django-base -f Dockerfile_django_base .


#####################################################################################
### Create the Nginx image and start the services
###
### Use the run_daphne_prd with the migrations on and create the base tables
echo "  "
echo "***** Docker compose / create Nginx image"
echo "  "
cd $BASE_DIR
docker-compose -f docker-compose_prd.yml up --build


#####################################################################################
### Add a job to cron, that will run the daily backup in the postgres images
### Note: /data/backup of the server will be mouted to /tmp in the postgres image
### Also create a job that will copy the latest backup to the NAS
### Ensure to add an empty line ??
### Every hour in minute 22 and 23
### !!! MAKE SURE ADMIN kan access the NAS
cp ./backup_psql_daily.sh /data/backup/backup_psql_daily.sh

### Create script with variables that copies the backup to the NAS.
### Note: Use single quotes to make a string. With double quotes the variables/characters will be interpreted 
# touch $RSYNC_SCRIPT
# echo '#!/bin/bash' >> $RSYNC_SCRIPT
# echo 'rsync -rvz /data/backup/$(ls -t /data/backup |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_daily.dump" >> $RSYNC_SCRIPT
# chmod +x $RSYNC_SCRIPT

### Note: the $(ls -t.. is in single quotes, so will not be interpreted will writing to cron.
### The $NAS_HOST part is in double quotes, so the actual address will be filled in
### Make a daily backup at 02:20 and copy to NAS at 02:25
### For every day in the week backup to a new file
crontab -l | { cat; echo '20 2 * * * docker exec -t klaverjas_psql_prd /tmp/backup_psql_daily.sh'; } | crontab -
crontab -l | { cat; echo '25 2 * * 0 rsync -rvz /data/backup/$(ls -t /data/backup |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_0.dump"; } | crontab -
crontab -l | { cat; echo '25 2 * * 1 rsync -rvz /data/backup/$(ls -t /data/backup |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_1.dump"; } | crontab -
crontab -l | { cat; echo '25 2 * * 2 rsync -rvz /data/backup/$(ls -t /data/backup |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_2.dump"; } | crontab -
crontab -l | { cat; echo '25 2 * * 3 rsync -rvz /data/backup/$(ls -t /data/backup |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_3.dump"; } | crontab -
crontab -l | { cat; echo '25 2 * * 4 rsync -rvz /data/backup/$(ls -t /data/backup |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_4.dump"; } | crontab -
crontab -l | { cat; echo '25 2 * * 5 rsync -rvz /data/backup/$(ls -t /data/backup |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_5.dump"; } | crontab -
crontab -l | { cat; echo '25 2 * * 6 rsync -rvz /data/backup/$(ls -t /data/backup |grep D_backup.dump | head -1) admin@'"$NAS_HOST:/volume1/Backup_remote/klaverjas_day_6.dump"; } | crontab -
crontab -l | { cat; echo "#"; } | crontab -

# crontab -l | { cat; echo "25 2 * * * $RSYNC_SCRIPT"; } | crontab -

