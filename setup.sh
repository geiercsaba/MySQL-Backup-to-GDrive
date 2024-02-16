echo 'create new virtual environment if not exists'
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

echo 'activate the virtual environment'
source venv/bin/activate

echo 'install the required packages'
pip install --upgrade -r requirements.txt

echo 'create a cron job to run the script every day at 3:00 AM (if it doesnt exist)'
if ! crontab -l | grep -q "cd $(pwd) && ./venv/bin/python3 backup.py"; then
  (crontab -l ; echo "0 3 * * * cd $(pwd) && ./venv/bin/python3 backup.py") | crontab -
fi