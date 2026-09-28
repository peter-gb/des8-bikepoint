import os
import boto3
from dotenv import load_dotenv
import logging
from datetime import datetime

# Get all access info from dotenv
load_dotenv()
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

# Set up S3 Connection using boto3
s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

# Set up logging folder
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# Get timestamp for log file name
time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f'{log_dir}/{time_stamp}.log'

# Config of logging

logging.basicConfig(
    filename=log_filename,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger()
logger.info('Logger successfully initialised')

    # First test upload with just one file
    # file_to_upload = 'data/2026-07-08 17-34-17.json'
    # filename_s3 = '2026-07-08 17-34-17.json'
    # When successful, we can then do this properly with a for loop


# create list of files
files_to_upload = os.listdir('data')        

# Loop through files with try / excpet for pushing to s3
for file in files_to_upload:
    file_to_upload = f'data/{file}'
    try:
        s3_client.upload_file(file_to_upload,AWS_BUCKET_NAME,file)
        print(f'{file} uploaded successfully.')
        logger.info(f'{file} uploaded successfully.')
    except Exception as e:
        print(f'An error has occurred: {e}')
        logger.info(f'An error has occurred: {e}')


