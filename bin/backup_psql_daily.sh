#!/bin/bash  

###
 # This script will create a DAILY backup of the postgres database into a folder.
 # Script to be run in the postgres container.
 #
 # The filename of the backup is: date_backup_dump, where date is like "2020_11_12_21:17:26"
 #
 # This script rotate the backup files.
 # a max of x backup files will be stored in the folder.
 # Based on the oldest modify date the the oldest backup file will be removed when more than N files are present. 
###

### Set variables
BACKUP_DIR="/tmp"
N_BACKUP=7
BASE_NAME="_D_backup.dump"
GREP_STRING="grep $BASE_NAME"


### Create a new backup in the backup folder
cd $BACKUP_DIR
now=$(date +"%Y_%m_%d_%H:%M:%S")
pg_dump -U postgres db_klaverjas > $now$BASE_NAME

### Check the number of backup files in the folder

N_FILES=$(ls | $GREP_STRING | wc -l)
echo $N_FILES

# Delete the oldest modified backup file when there are more than allowed
if [ "$N_FILES" -gt "$N_BACKUP" ]; then
  rm "$(ls -t | $GREP_STRING | tail -1)"
  NEW_N=$(ls  | $GREP_STRING | wc -l)
  echo "$NEW_N backup files in the folder after backup"
fi