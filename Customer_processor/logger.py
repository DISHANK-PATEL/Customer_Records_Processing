import logging
from config import ERROR_LOG_FILE

def setup_logger():
    logger = logging.getLogger("CustomerProcessor")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(ERROR_LOG_FILE)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
