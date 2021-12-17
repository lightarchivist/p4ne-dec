import logging

# see https://docs.python.org/3/library/logging.html
# for more things you can put in the format
format = '%(name)s - %(levelname)s - %(message)s - %(asctime)s'

# we'll use a dictionary to pass the loggin configuration
my_logging_config = {
    'filename' : 'mylog3.txt',
    # 'a' = append is the default, but 'w' = overwrite is available
    'filemode' : 'a',
    # all events at or above DEBUG will get logged
    'level' : 'DEBUG',
    'format' : format,
    # to set the datetime format fi you want it different to the defualt
    'datefmt' : '%Y-%m-%d - %H:%M:%S' 
    }
# configure logging using the dictionay
logging.basicConfig(**my_logging_config)

# the following cause messages to be written to the log
logging.critical('Something Critical happened!')
logging.error('Something Error-like happened!')
logging.warning('You are being warned!')
logging.info('A little bit of info you might like')
logging.debug('Verbose debugging info to help you sort it all out...')

a = 5
b = 0
try:
    # the following causes an exeption
    c = a / b
except Exception as e:
    # the exception is logged
    # exc_info=True includes the exception traceback with the log message
    logging.error("Exception occurred", exc_info=True)

