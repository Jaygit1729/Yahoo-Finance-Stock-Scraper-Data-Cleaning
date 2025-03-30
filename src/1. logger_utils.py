import logging
import os

def setup_logger(log_file):

    """ Set up a logger that writes logs to a file and prints them to the console"""

    logger  = logging.getLogger(log_file)
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        os.makedirs(os.path.dirname(log_file),exist_ok= True)
        file_handler = logging.FileHandler(log_file)
        stream_handler = logging.StreamHandler()

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger
