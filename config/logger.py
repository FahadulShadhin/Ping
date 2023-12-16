# config/logger_config.py
import logging


def logger_config():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        handlers=[logging.StreamHandler()]
    )
    return logging.getLogger(__name__)
