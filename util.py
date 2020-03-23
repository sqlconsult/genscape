"""Utilities"""
from pathlib import Path
import logging

import logger

# file_meta_data:
#     file_name   = file name to read
#     delimiter   = field delimiter in that file
#     col_mapping = mapped column name in solumn number order
FILE_META_DATA = [
    {'file_name': 'csv',
     'delimiter': ',',
     'col_mapping': ['title', 'last_name', 'first_name', 'publication_date']},
    {'file_name': 'pipe',
     'delimiter': '|',
     'col_mapping': ['first_name', 'last_name', 'title', 'publication_date']},
    {'file_name': 'slash',
     'delimiter': '/',
     'col_mapping': ['publication_date', 'first_name', 'last_name', 'title']}]

def start_logger(app_name, calling_function):
    """
    Create logging directory along with starting module logger
    :param  calling_function   Name of calling function - used for log file name
    """
    # Create logs directory if not present
    Path('logs').mkdir(parents=True, exist_ok=True)

    # Start logger
    logger.start_logger(app_name)

    module_logger = logging.getLogger('{app_name}.{calling_function}'.\
        format(app_name=app_name, calling_function=calling_function))

    return module_logger
