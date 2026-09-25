# import packages dor the script

import requests
import json
import os
from datetime import datetime
import time

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

while attempt < max_retry:

    # make a request to the TFL API and get the response
    response = requests.get(url)
    print(response.status_code)

    # save the response data to a JSON file
    data = response.json()
    with open(filename, "w") as file:
        json.dump(data, file)


    # do some error handling based on the status code of the response
    status = response.status_code

    if 200 <= status < 300:
        print(f'File {filename} was successfully saved')
        break
    elif status < 200 or status >= 500:
        print(f'Status code {status}')
        break   
    else:
        print(f'Error - Status code{status}. Fix it!!!')
        attempt += 1
        break

