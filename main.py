from modules.log_initialise import setup_logging
from modules.extract_function import extract_json
from modules.load_function import load_files_to_s3
from datetime import datetime
from dotenv import load_dotenv
import os

# make timestamp string which is used by all functions
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

# use the logging function to define where the logs go
logger = setup_logging('logs', timestamp)

# send a logging message to say we're up and running
logger.info('Logger successfully initialised.')

#define our url to get the data from the TFL API
url = "https://api.tfl.gov.uk/BikePoint"

# create a directory to store the data if it doesn't exist
data_dir = "data"

# retry settings for extract
max_retry = 5
delay = 10  

# use extract function to extract
extract_json(url, data_dir, timestamp, max_retry, delay)


# Get all access info from dotenv
load_dotenv()
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

# use load function to send it to s3
load_files_to_s3(data_dir, AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME)