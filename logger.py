"""Logging module"""
import datetime
import logging


def start_logger(app_name):
    """
    Create logger & add handlers
    :param app_name     Name of app creating logger & handlers
    """
    # Create logger with 'spam_application'
    logger = logging.getLogger(app_name)
    logger.setLevel(logging.DEBUG)

    # Create file handler which logs debug messages
    log_fil_nm = 'logs/monitor_log_{date:%Y%m%d_%H%M%S}.log'.format(date=datetime.datetime.now())
    file_handler = logging.FileHandler(log_fil_nm)
    file_handler.setLevel(logging.DEBUG)

    # Create console handler with a higher log level, error
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter(\
        '%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
