# Created: 2024-07
# Created by: Basile El Azhari
# Maintained by: Basile El Azhari
# Contact: basile.elazhari@ekimetrics.com, https://www.linkedin.com/in/basile-el-azhari/

import os
import logging
from datetime import datetime
from typing import Optional

from .settings import get_settings


settings = get_settings()
LOG_FILE_PATH = settings.LOG_FILE_PATH
LOG_DATETIME_FORMAT = settings.LOG_DATETIME_FORMAT
LOG_FORMAT = settings.LOG_FORMAT

logging.basicConfig(level=logging.INFO)


def compute_log_file_path(log_file_path: str, log_datetime_format: str) -> str:
    """
    Compute the log file path, including an hour timestamp at the end
    :param log_file_path: The name of the file to log to.
    :param log_datetime_format: The format of the datetime to append to the log file name.
    :return: The log file path.
    """
    return log_file_path.replace(
        "[DATETIME_PLACEHOLDER]",
        f"{datetime.now().strftime(log_datetime_format)}",
    )


def create_logger(
    log_format: str,
    log_file_path: Optional[str] = LOG_FILE_PATH,
    log_datetime_format: Optional[str] = LOG_DATETIME_FORMAT,
) -> logging.Logger:
    """
    Create a logger to log to the console and eventually to a file.
    :param log_format: The format of the log. If None, the default format will be used.
    :param log_file_path: The name of the file to log to. If None, no log file will be created.
    :param log_datetime_format: The format of the datetime to append to the log file name. Must be specified if log_file_path is not None.
    :return: A logger.
    """
    # Create a custom logger
    logger_ = logging.getLogger(__name__)

    # Create handlers
    c_handler = logging.StreamHandler()

    # Create formatters and add it to handlers
    c_format = logging.Formatter(fmt=log_format)

    # Add formatters to handlers
    c_handler.setFormatter(c_format)

    # Add handlers to the logger_
    logger_.handlers.clear()
    logger_.addHandler(c_handler)

    # Add file handler if log_file_path is provided
    if log_file_path:
        log_file_path_ = log_file_path if log_file_path else ""
        log_datetime_format_ = log_datetime_format if log_datetime_format else ""
        # Create the directories if they do not exist
        os.makedirs(os.path.dirname(log_file_path_), exist_ok=True)
        print(f"Logging to {log_file_path_}")

        # Compute the log file path with timestamp
        log_file_path_ts = compute_log_file_path(log_file_path_, log_datetime_format_)

        # Create the file handler
        f_handler = logging.FileHandler(log_file_path_ts, mode="a+", encoding="utf-8")
        f_format = logging.Formatter(fmt=log_format)
        f_handler.setFormatter(f_format)
        logger_.addHandler(f_handler)

    return logger_


logger = create_logger(LOG_FORMAT, LOG_FILE_PATH, LOG_DATETIME_FORMAT)

# Log environment variables
logger.info("Printing environment variables")
logger.info(f"LOG_FORMAT: {LOG_FORMAT}")
logger.info(f"LOG_FILE_PATH: {LOG_FILE_PATH}")
logger.info(f"LOG_DATETIME_FORMAT: {LOG_DATETIME_FORMAT}")

