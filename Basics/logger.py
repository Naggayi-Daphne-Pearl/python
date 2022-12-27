import logging

# Set the log level
# Set the log level and log file
logging.basicConfig(level=logging.INFO, filename="dictionary.py", format="%(asctime)s %(levelname)s: %(message)s")

# Create a logger
logger = logging.getLogger(__name__)

# Use the logger
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message")

