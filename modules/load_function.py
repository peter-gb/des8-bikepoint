import os
import boto3
from dotenv import load_dotenv
import logging
from datetime import datetime


logger = logging.getLogger(__name__)

def load_files_to_s3(data_dir:str, AWS_ACCESS_KEY:str, AWS_SECRET_ACCESS_KEY:str, AWS_BUCKET_NAME:str):
    """Uploads all files in the data directory to S3.

    Args:
        data_dir (str): where the data is
        AWS_ACCESS_KEY (str): linked to AWS IAM user
        AWS_SECRET_ACCESS_KEY (str): linked to AWS IAM user
        AWS_BUCKET_NAME (str): S3 bucket to upload to
    """

    # Set up S3 Connection using boto3
    s3_client = boto3.client(
        's3',
        aws_access_key_id = AWS_ACCESS_KEY,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )

    # create list of files
    files_to_upload = os.listdir(data_dir)        

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