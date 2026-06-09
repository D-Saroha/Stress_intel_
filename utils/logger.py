import logging
import os

from config import Config


os.makedirs(Config.LOG_DIR, exist_ok=True)


def get_logger(name):

    logger = logging.getLogger(name)

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler = logging.FileHandler(
            Config.APP_LOG_PATH
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger