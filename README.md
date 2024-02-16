### MySQL DB Backup
This repository contains a script to backup a MySQL database to Google Drive using the Google Drive API. 
The script is written in Python and uses the `google-api-python-client` library to interact with the Google Drive API.
The script is designed to be run as a cron job on a Linux server.

### How to setup
1. Clone the repository to your local machine
2. Go to the [Google Developers Console](https://console.developers.google.com/) and create a new project
3. Enable the Google Drive API for the project
4. Create a new [Service Account](https://console.cloud.google.com/apis/credentials) and download the credentials JSON file
5. Share the folder you want to backup to with the service account email
6. Edit the `.config` file and add the path to the credentials JSON file
7. Run the `setup.sh` script to setup project and cron job

### How to run
The script is designed to be run as a cron job. The `setup.sh` script will add a new cron job to the crontab. 
The cron job will run the `backup.py` script at 3am every day by default.
