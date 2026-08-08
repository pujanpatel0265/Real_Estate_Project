import logging
import os


def setup_logger():
    # Create the logs folder if it does not exist
    os.makedirs("logs", exist_ok=True)

    # Set up the log file
    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger(__name__)

#This file sets up logging for my project.
# It creates an app.log file inside the logs folder.
# Other modules can use this logger to record successful operations and errors, which helps with debugging.