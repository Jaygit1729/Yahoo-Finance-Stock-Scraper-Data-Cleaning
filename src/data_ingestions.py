from logger_utils import setup_logger
import os
import pandas as pd
import numpy as np



# Define base directory (Project Root)

BASE_DIR = os.getcwd()  

def get_full_path(relative_path):

    """Helper function to get the full path of a file inside the project directory"""
    return os.path.join(BASE_DIR, relative_path)

logger = setup_logger("logs/data_ingestions")
logger.info("Logging set up successfully for data ingestions")

def load_data(file_path):

    """Loads Datasets from the csv file"""

    try:
        if not os.path.exists(file_path):
            logger.error(f"File not Found:{file_path}")
            return None
        df = pd.read_csv(file_path)
        logger.info(f"Data Loaded Successfully from {file_path}")
        return df 
    
    except Exception as e:
        logger.error(f"Error Loading Data from {file_path}: {e}")

def save_data(df, output_path):

    """"Saves the dataset to the specified output path."""
    
    full_path = get_full_path(output_path)  # Convert relative to absolute path

    try:
        os.makedirs(os.path.dirname(output_path), exist_ok= True)
        df.to_csv(output_path,index = False)
        logger.info(f"Data Saved Successfully to {output_path}")
    
    except Exception as e:
        logger.error(f"Error Saving data to {output_path}: {e}")

if __name__ ==  "__main__":

    df = load_data(r"data/raw_stocks_details.csv")
    if df is not None:
        save_data(df, r"data/stocks_details.csv")
    print(df.head())