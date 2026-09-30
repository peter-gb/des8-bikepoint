import os
import logging
# from datetime import datetime

def setup_logging(log_dir:str, timestamp:str):
    """This will initialise the logger.

    Args:
        log_dir (str): where you want your logs saved
        timestamp (str): the timestamp will be the name of the log file
    """
    # prepare logging
    # create folder for logging if it doesn't exist, prepare log filename with timestamp
    os.makedirs(log_dir, exist_ok=True)
    log_filename = f'{log_dir}/{timestamp}.log'

    # configure logging file and messages
    logging.basicConfig(
        filename=log_filename,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    # create the logger and confirm that it is successfully set up
    return logging.getLogger()