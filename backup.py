import configparser
import os.path
import time
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import subprocess
import logging

logging.basicConfig(filename='./backup.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# read .config file
if not os.path.isfile('.config'):
    logging.error('.config file not found in the current directory: ', os.getcwd())
    raise FileNotFoundError('.config file not found in the current directory: ', os.getcwd())

current_time = time.strftime("%Y_%m_%d")
config = configparser.ConfigParser()
config.read('.config')

# Backup database
logging.info('Backup database')
command = f"mysqldump -u{config['Database']['user']} -p'{config['Database']['password']}' --databases {config['Database']['databases']} --result-file=./{current_time}_backup.sql"
subprocess.run(command, shell=True)

# Google Drive API
logging.info('Google Drive API - Create connection')
scopes = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(config['GoogleDrive']['cred_file'], scopes=scopes)
service = build("drive", "v3", credentials=creds)

file_metadata = {
    'name': 'db_backup_' + current_time + '.sql',
    'parents': [config['GoogleDrive']['backup_folder']]
}

logging.info('Google Drive API - Upload file')
media = MediaFileUpload(f"./{current_time}_backup.sql", resumable=True, mimetype='application/mysql')
file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

logging.info('Remove local file')
os.remove(f"./{current_time}_backup.sql")