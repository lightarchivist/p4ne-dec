
# source: https://realpython.com/python-logging/logging_example.py

import logging
# The name of the logger can be in the events.
logger = logging.getLogger('mylogger')

# All the configuration of the logger can be done using a config file or by using 
# the classes/methods below.

# Create handlers
c_handler = logging.StreamHandler() # prints to console
f_handler = logging.FileHandler('file.log') # prints to file
# set the level, the handler gets that level and above
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger so that when the logger creates a log entry
# it gets handled by them.
logger.addHandler(c_handler)
logger.addHandler(f_handler)

#  The logger creates a warning and an error.
logger.warning('This is a warning')
logger.error('This is an error')

