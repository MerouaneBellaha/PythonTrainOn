<!-- virtual env + requirements setup -->

sudo python3 -m pip install virtualenv
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
pip install -r requirements.txt
# deactivate

<!-- run -->

source var.env
python3 ./get\ test.py