# .../base/logging/my_logging.py

import logging
import os
import sys

from django.conf import settings

# get the base folder from the settings file
# Go one folder up and then to log 
base_dir = settings.BASE_DIR
path_up = os.path.dirname(base_dir)
log_dir = os.path.join(path_up, "log")

# Log settings
min_level 	= settings.MIN_LOG_LEVEL
maxSize 	= 50000000
backupCount = 5

# Define the loggger and the handlers
# Everything should be propagated to root, so root logs everything
# Only root will display to console. Also it will store to a rotating file.
# All other loggers will only store to file.
# Some of these files are rotating

LOG_CONFIG = {
	'version': 1, 
	'formatters': {
		'simple': {
			'format': '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
		}, 
		'enhanced': {
			'format': '%(asctime)s - %(levelname)s - %(name)s - %(message)s - [%(lineno)d] - %(pathname)s'
		}
	}, 
	'handlers': {
		'console-simple': {
			'class': 'logging.StreamHandler', 
			'level': min_level, 
			'formatter': 'simple', 
			'stream': 'ext://sys.stdout'
		}, 
		'console-enhanced': {
			'class': 'logging.StreamHandler', 
			'level': min_level, 
			'formatter': 'enhanced', 
			'stream': 'ext://sys.stdout'
		},
    'registration_file': {
			'class': 'logging.FileHandler', 
			'level': 'INFO', 
			'formatter': 'simple', 
			'filename': os.path.join(log_dir, "registration.log"),
			'mode': 'a'
		},
		'error_file': {
			'class': 'logging.handlers.RotatingFileHandler', 
			'level': 'ERROR', 
			'formatter': 'enhanced', 
			'filename': os.path.join(log_dir, "errors.log"),
			'maxBytes': maxSize,
			'backupCount': backupCount,
			'encoding': 'utf8'
		},
		'authentication_file': {
			'class': 'logging.handlers.RotatingFileHandler', 
			'level': 'INFO', 
			'formatter': 'simple', 
			'filename': os.path.join(log_dir, "auth.log"),
			'maxBytes': maxSize,
			'backupCount': backupCount,
			'encoding': 'utf8'
		},
		'debug_file': {
			'class': 'logging.handlers.RotatingFileHandler', 
			'level': min_level, 
			'formatter': 'enhanced', 
			'filename': os.path.join(log_dir, "debug.log"),
			'maxBytes': maxSize,
			'backupCount': 1,
			'encoding': 'utf8'
		},
		'default_file': {
			'class': 'logging.handlers.RotatingFileHandler', 
			'level': min_level, 
			'formatter': 'enhanced', 
			'filename': os.path.join(log_dir, "default.log"),
			'maxBytes': maxSize,
			'backupCount': 1,
			'encoding': 'utf8'
		},
		'trace_file': {
			'class': 'logging.handlers.RotatingFileHandler', 
			'level': min_level, 
			'formatter': 'simple', 
			'filename': os.path.join(log_dir, "trace.log"),
			'maxBytes': maxSize,
			'backupCount': 1,
			'encoding': 'utf8'
		},
		'action_file': {
			'class': 'logging.handlers.RotatingFileHandler', 
			'level': min_level, 
			'formatter': 'simple', 
			'filename': os.path.join(log_dir, "action.log"),
			'maxBytes': maxSize,
			'backupCount': 1,
			'encoding': 'utf8'
		},
		'root_file': {
			'class': 'logging.handlers.RotatingFileHandler',
			'level': min_level,
			'formatter': 'enhanced',
			'filename': os.path.join(log_dir, "root.log"),
			'maxBytes': maxSize,
			'backupCount': backupCount,
			'encoding': 'utf8'
		}
	}, 
	'loggers': {
		'console_only': {
			'level': min_level, 
			'handlers': ['console-enhanced'], 
			'propagate': False
		},
		'default': {
			'level': min_level, 
			'handlers': ['default_file'], 
			'propagate': True
		},
		'trace': {
			'level': min_level, 
			'handlers': ['trace_file'], 
			'propagate': True
		},
		'action': {
			'level': min_level, 
			'handlers': ['action_file'], 
			'propagate': True
		},
    'registration': {
			'level': 'INFO', 
			'handlers': ['registration_file'], 
			'propagate': True
		},
		'authentication': {
			'level': 'INFO', 
			'handlers': ['authentication_file'], 
			'propagate': True
		},
		'errors': {
			'level': 'ERROR', 
			'handlers': ['error_file'], 
			'propagate': True
		},
		'debug': {
			'level': min_level, 
			'handlers': ['debug_file'], 
			'propagate': True
		}
	}, 
	'root': {
		'level': min_level, 
		'handlers': ['console-enhanced', 'root_file']
	}
}


def create_logger(logger_name='not_set'):
	'''
	Create a logger. 
	When a logger_name is given, a logger as defined in the LOG_CONFIG dictionairy will be created
	When no, or no valid logger_name is given then a default logger is created

	examples:
		logger = create_logger('logger1')
		logger = create_logger()		# will create a default logger
	'''

	# Check that the logger name exist in the config dict.
	if logger_name in LOG_CONFIG['loggers']:

		# Create the logger with this name
		logging.config.dictConfig(LOG_CONFIG)
		logger = logging.getLogger(logger_name)

		return logger

	else:
		# Create the default logger to file
		logging.config.dictConfig(LOG_CONFIG)
		logger = logging.getLogger('default')

		return logger


def logger(logger_name='not_set'):
	'''
	Create a logger. 
	When a logger_name is given, a logger as defined in the LOG_CONFIG dictionairy will be created
	When no, or no valid logger_name is given then a default logger is created

	examples:
		logger = create_logger('logger1')
		logger = create_logger()		# will create a default logger
	'''

	# Check that the logger name exist in the config dict.
	if logger_name in LOG_CONFIG['loggers']:

		# Create the logger with this name
		logging.config.dictConfig(LOG_CONFIG)
		logger = logging.getLogger(logger_name)

		return logger

	else:
		# Create the default logger to file
		logging.config.dictConfig(LOG_CONFIG)
		logger = logging.getLogger('default')

		return logger