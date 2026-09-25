# import packages dor the script

import requests
import json
import os
from datetime import datetime

#define our url to get the data from the TFL API
url = "https://api.tfl.gov.uk/BikePoint"

# make a request to the TFL API and get the response
response = requests.get(url)
print(response.status_code)

# create a directory to store the data if it doesn't exist
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# get the current date and time to use in the filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{data_dir}/bikepoint_data_{timestamp}.json"

# save the response data to a JSON file
data = response.json()
with open(filename, "w") as file:
    json.dump(data, file)


# do some error handling based on the status code of the response
status = response.status_code

if 200 <= status < 300:
    print(f'File {filename} was successfully saved')
elif status < 200 or status >= 500:
    print(f'Status code {status}')
else:
    print(f'Error - Status code{status}. Fix it!!!')

