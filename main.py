from modules.log_initialise import setup_logging
from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

logger = setup_logging('logs', timestamp)
logger.info('Logger successfully initialised.')