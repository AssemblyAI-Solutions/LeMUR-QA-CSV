import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log_file = './logs.txt'

file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)