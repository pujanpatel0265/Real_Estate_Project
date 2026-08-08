import pandas as pd
from src.logger import setup_logger


logger = setup_logger()


def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logger.info("Dataset loaded successfully.")
        return data

    except Exception as error:
        logger.error(f"Error loading dataset: {error}")
        raise
    
#data_loader.py is responsible only for loading the CSV dataset.
# I separated it from the model code to make the project modular.
# I also added try/except so any loading error is recorded in the log file