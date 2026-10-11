# logging: levels, configuration, handlers, formatters, and stack traces
import logging

# 1. Built-in log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
# By default, only WARNING and above are printed
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S'
)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#  Creating a custom logger for modules
logger = logging.getLogger(__name__)

#  Log Handlers (StreamHandler for console, FileHandler for files)
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')

# Set specific log level thresholds for each handler
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

#Custom Formatter for handlers
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning("This warning goes to console")
logger.error("This error goes to console AND app.log")

# Capturing Stack Traces in Logs
try:
    items = [1, 2, 3]
    val = items[4]
except IndexError as e:
    # exc_info=True includes full traceback in the log output
    logger.error("Index out of range occurred", exc_info=True)