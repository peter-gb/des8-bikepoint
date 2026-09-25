# import packages dor the script

import requests
import json
import os
from datetime import datetime
import time
import logging

#define our url to get the data from the TFL API
url = "https://api.tfl.gov.uk/BikePoint"


# create a directory to store the data if it doesn't exist
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# get the current date and time to use in the filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{data_dir}/bikepoint_data_{timestamp}.json"


# setup a retry mechanism in case the request fails

max_retry = 5
attempt = 0
delay = 10

# prepare logging
# create folder for logging if it doesn't exist, prepare log filename with timestamp
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_filename = f'{log_dir}/extract{timestamp}.log'

# configure logging file and messages
logging.basicConfig(
    filename=log_filename,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger()
logger.info('Logger successfully initialised')

#make the API calls, inside a loop that will retry the request if it fails, up to a maximum number of attempts
while attempt < max_retry:

    # make a request to the TFL API and get the response
    response = requests.get(url)
    print(response.status_code)
    logger.info(f'API request made. Response status code: {response.status_code}')

    # save the response data to a JSON file
    data = response.json()
    with open(filename, "w") as file:
        json.dump(data, file)


    # do some error handling based on the status code of the response
    status = response.status_code

# on success
    if 200 <= status < 300:

        # check if the data is empty and print a warning message if it is
        if len(data) > 0:
            try:
                with open(filename, 'w') as file:
                    json.dump(data, file)
                    print(f'File {filename} was successfully saved')
                    logger.info(f'File {filename} was successfully saved')


            except Exception as e:
                print(f'An error occurred: {e}')
                logger.error(f'An error occurred while saving the file: {e}')
            break
        else:
            print(f'Warning: The data is empty. Check the API response.')
            logger.warning(f'Warning: The data is empty. Check the API response.')
            break

# on error, retry after a delay
    elif status < 200 or status >= 500:
       
        # wait for a delay before retrying
        time.sleep(delay)
        attempt += 1
        print(f'Status code {status}. Retrying. This was attempt {attempt}')
        logger.warning(f'Status code {status}. Retrying. This was attempt {attempt}')

# unknown error, break the loop and print an error message
    else:
        print(f'Error - Status code{status}. Fix it!!!')
        logger.error(f'Error - Status code{status}. Fix it!!!')
        break

