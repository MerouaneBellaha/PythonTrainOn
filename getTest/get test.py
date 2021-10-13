#!/usr/local/bin/python3

# pythonTestApi

import logging

# ASK: what is __name__
log = logging.getLogger(__name__) 
from logging.handlers import RotatingFileHandler

import requests
import time
import os
import sys
from datetime import datetime

# ------------------------------
# LOGpip
# ------------------------------
LOG_FILE_LEVEL       = 'DEBUG'
LOG_STDOUT_LEVEL     = 'INFO'
LOG_FILE_NB_MAX_BYTE = 10000000
# ------------------------------

# ------------------------------
# SCRIPT FILE INFO
# ------------------------------
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
SCRIPT_NAME = os.path.basename(sys.argv[0])

# ------------------------------
# CONSTANT
# ------------------------------
INPUT_FILEPATH               = './input.csv'
SLEEP_TIME_RETRY_REQUEST_SEC = 1
NB_TRY_REQUEST               = 3
NB_OF_OBJECT_LIMIT = 1

BASE_URL_KEY = 'BASE_URL'
API_KEY_KEY = 'API_KEY'

# ------------------------------
# UTILS
# ------------------------------
def sourceEnvLog(key):
    return f'You need to source environment variables (no {key} found in OS env)'

# ------------------------------
# LOG
# ------------------------------
def setLog():
    logger = logging.getLogger()
    logger.setLevel(LOG_FILE_LEVEL)
    formatter = logging.Formatter('%(asctime)s %(process)d %(levelname)s %(message)s')
    logFile = os.path.join(SCRIPT_PATH, os.path.splitext(SCRIPT_NAME)[0] + '{}'.format(datetime.now().strftime("%Y-%m-%dT%H:%M:%S")) + '.log')
    file_handler = RotatingFileHandler(logFile, 'a', LOG_FILE_NB_MAX_BYTE, 1)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(LOG_STDOUT_LEVEL)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

# ------------------------------
# ENVIRONEMENT VARIABLE
# ------------------------------
def setEnvVar():
    (base_url, api_key) = ('', '')
    if BASE_URL_KEY in os.environ:
        base_url = os.environ[BASE_URL_KEY]
    else:
        log.error(sourceEnvLog(BASE_URL_KEY))
        sys.exit(1)

    if API_KEY_KEY in os.environ:
        api_key = os.environ[API_KEY_KEY]
    else:
        log.error(sourceEnvLog(API_KEY_KEY))
        sys.exit(1)

    return (base_url, api_key)

# ------------------------------
# API CALL
# ------------------------------
def getGifForQuery(log, base_url, api_key, query):
#ASK: why .format

  end_point = f'{base_url}gifs/search?api_key={api_key}&q={query}&limit={NB_OF_OBJECT_LIMIT}'

#   headers                 = {}
#   headers['Accept']       = 'application/json'
#   headers['Content-Type'] = 'application/json'
#   payload                 = {}

  status_ok               = [200]

  number_of_try_request = 0
  status = 0
  response = None    

  while (status not in status_ok) and number_of_try_request <= NB_TRY_REQUEST:
    try:    
      response = requests.get(end_point)
    except requests.exceptions.RequestException as e:
      log.warning("Fail call API {} : {}".format(end_point, e))
      time.sleep(SLEEP_TIME_RETRY_REQUEST_SEC)
      continue
    status = int(response.status_code)
    if status not in status_ok:
      log.warning('{} : [{}]{}'.format(query, response.status_code, response.text.rstrip()))
      log.debug('{} : [{}]{} ({})'.format(query, response.status_code, response.text.rstrip(), response.headers))
      time.sleep(SLEEP_TIME_RETRY_REQUEST_SEC)
    if number_of_try_request >= NB_TRY_REQUEST:
      log.error('Fail to get a 200 HTTP response on : {}, nb_retry={}'.format(end_point, NB_TRY_REQUEST))
    number_of_try_request += 1

    result = '{};{};{}'.format(query, response.status_code, response.text.rstrip())
    log.debug(result)
  return response.json()


def main():
    setLog()
    (base_url, api_key) = setEnvVar()

    with open(INPUT_FILEPATH, 'r') as input_file:
        input_file_content = input_file.read().splitlines() 
        result_file = os.path.join(SCRIPT_PATH, 'ouput_' + os.path.splitext(SCRIPT_NAME)[0] + '.csv')

        with open(result_file, 'w') as result_file_content:
            for line in input_file_content:
                if not line.startswith("#"):
                    response = getGifForQuery(log, base_url, api_key, line)
                    
                    gifUrl = response['data'][0]['url']
                    log.info(gifUrl)
                    result_file_content.write(f'{gifUrl}\n')

        time.sleep(SLEEP_TIME_RETRY_REQUEST_SEC) 
    
main()