import logging

logger = logging.getLogger("automation_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)