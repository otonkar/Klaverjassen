#!/bin/bash  

###
 # This script will create a DAILY backup of the postgres database into a folder.
 # Script to be run in the postgres container.
 #
 # The filename of the backup is: date_D_backup.dump, where date is like "2020_11_12_21-17-26"
 # Note: do not use character ':' in the time, because this will give issues in the command to copy this file
 # because \: must be used to escape this special character
 #
 # This script rotates the backup files.
 # a max of N_BACKUP backup files will be stored in the folder.
 # Based on the oldest modify date the oldest backup file will be removed when more than N files are present. 
 # NOTE: when there are already more files, still only 1 will be removed (later add a while loop)
###

### Set variables
# folder where the backups are created
# BACKUP_DIR="/tmp"       #for in docker images
BACKUP_DIR="/var/backups/psql"
# the number of backups that must be kept before overwriting
N_BACKUP=1
# the name of the backup.
BASE_NAME="_D_backup.dump"

GREP_STRING="grep $BASE_NAME"


### Create a new backup in the backup folder
cd $BACKUP_DIR
now=$(date +"%Y_%m_%d_%H-%M-%S")
sudo -u postgres pg_dump db_klaverjas > $now$BASE_NAME
# sudo pg_dump -U postgres db_klaverjas > $now$BASE_NAME


### Check the number of backup files in the folder

N_FILES=$(ls | $GREP_STRING | wc -l)
echo $N_FILES

# Delete the oldest modified backup file when there are more than allowed
# if [ "$N_FILES" -gt "$N_BACKUP" ]; then
#   rm "$(ls -t | $GREP_STRING | tail -1)"
#   NEW_N=$(ls  | $GREP_STRING | wc -l)
#   echo "$NEW_N backup files in the folder after backup"
# fi


while [ "$N_FILES" -gt "$N_BACKUP" ] ; do
  rm "$(ls -t | $GREP_STRING | tail -1)"
  NEW_N=$(ls  | $GREP_STRING | wc -l)
  echo "$NEW_N backup files in the folder after backup"
  # get the new numver of files
  N_FILES=$(ls | $GREP_STRING | wc -l)
done

# Note: rsync within a postgres docker container does not work.
# Therefore on the server an additional job must be run to upload the backup