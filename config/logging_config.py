#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from functools import reduce

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# range:当前文件往上几层
BASE_DIR = reduce(lambda x, y: os.path.dirname(x), range(2), os.path.abspath(__file__))

# Logging settings Begin
LOGGING_FILE_PATH = os.path.join(BASE_DIR, 'logs') if BASE_DIR else os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGGING_FILE_PATH):
    os.makedirs(LOGGING_FILE_PATH)
LOGGING = {
    'disable_existing_loggers': True,
    'version': 1,
    'formatters': {
        'standard': {
            # INFO 2016-09-03 16:25:20,067 /home/ubuntu/mysite/views.py views.py views get 29: some info...
            'format': '%(levelname)s %(asctime)s %(pathname)s %(module)s %(funcName)s %(lineno)d: ' +
                      '%(message)s'
        },
        'simple': {
            # INFO 2016-09-03 16:25:20,067 /home/ubuntu/mysite/views.py views.py views get 29: some info...
            'format': '%(asctime)s %(message)s',
            'datefmt': '%Y %b %d-%H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_FILE_PATH, 'debug.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_FILE_PATH, 'error.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'spider_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_FILE_PATH, 'spider.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'db_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_FILE_PATH, 'databases.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True,  # this tells logger to send logging message
            # to its parent (will send if set to True)
        },
        'console': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'spider': {
            'handlers': ['spider_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
        'sql_db': {
            'handlers': ['db_handler'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}
# Logging settings End