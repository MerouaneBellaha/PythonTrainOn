#!/usr/local/bin/python3

# pythonTestApi

import logging

# ASK: what is __name__
log = logging.getLogger(__name__) 


import requests
from requests.auth import HTTPBasicAuth
import json
import time
import os
import sys
import argparse
from datetime import datetime

# # ------------------------------
# # LOGpip
# # ------------------------------
# LOG_FILE_LEVEL       = 'DEBUG'
# LOG_STDOUT_LEVEL     = 'INFO'
# LOG_FILE_NB_MAX_BYTE = 10000000
# # ------------------------------
# # WHERE AM I, WHO AM I
# # ------------------------------
# SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
# SCRIPT_NAME = os.path.basename(sys.argv[0])


# ------------------------------
# CONSTANT
# ------------------------------
INPUT_FILEPATH               = './input.csv'
SLEEP_TIME_RETRY_REQUEST_SEC = 1
NB_TRY_REQUEST               = 3

pomme='pomme'


def main():

    if 'BASE_URL' in os.environ:
        base_url = os.environ['BASE_URL']
    else:
        log.error('You need to source environment variables (no BASE_URL found in OS env)')
        sys.exit(1)

    if 'API_KEY' in os.environ:
        api_key = os.environ['API_KEY']
    else:
        log.error('You need to source environment variables (no API_KEY found in OS env)')
        sys.exit(1)

    
main()