# logger.py
import logging
import sys
import os

def setup_logger(name="run_tests", log_dir=None, console_level=logging.INFO):
    """
    Set up a logger with both console and file handlers.

    Args:
        name: Logger name (string)
        log_dir: Directory to store log file (default: current working directory)
        console_level: Logging level for console output

    Returns:
        logger: Configured logger instance
        log_file_path: Full path to the log file (string)
    """
    if log_dir is None:
        log_dir = os.getcwd()
    else:
        os.makedirs(log_dir, exist_ok=True)

    log_file_path = os.path.join(log_dir, "run_tests.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Let handlers filter
    logger.handlers.clear()  # Remove any existing handlers
    logger.propagate = False

    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )

    # Console handler
    console = logging.StreamHandler(stream=sys.stdout)
    console.setLevel(console_level)
    console.setFormatter(formatter)

    # File handler (overwrites each run)
    file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger, log_file_path