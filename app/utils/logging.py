from logging.handlers import RotatingFileHandler
from logging import StreamHandler
from pathlib import Path
import logging
import os

log_folder_path = str(Path('logs').absolute())

if not os.path.exists(log_folder_path):
    os.makedirs(log_folder_path)

log_file_path = os.path.join(log_folder_path, 'log.out')

log_fmt = '%(threadName)s - %(asctime)s - %(name)s - ' \
          '%(levelname)s - %(message)s'

logger_formatter = logging.Formatter(log_fmt)

file_logger = RotatingFileHandler(log_file_path, maxBytes=1024*1024*10,backupCount=5)
file_logger.setLevel(logging.DEBUG)
file_logger.setFormatter(logger_formatter)

client_logger = StreamHandler()
client_logger.setLevel(logging.INFO)
client_logger.setFormatter(logger_formatter)
