from logger_utils import setup_logger
from data_ingestions import load_data, save_data
import pandas as pd
import numpy as np
import os

# Setup logger
logger = setup_logger("logs/data_cleaning")
logger.info("Logging set up successfully for data cleaning")

def clean_yahoo_finance_data(data):
    """
    Cleans the scraped stock data from Yahoo Finance.

    """
    
    stocks_df = (pd
        .DataFrame(data = data)
        .apply(lambda col:col.str.strip() if col.dtype =='object' else col)
        .assign(      
            Change_in_pct   =  lambda df_:pd.to_numeric(df_.Change_in_pct.str.replace("+","").str.replace("%","")),
            Volume          =  lambda df_:pd.to_numeric(df_.Volume.str.replace("M","")),
            Avg_Vol_Per_3M  =  lambda df_:pd.to_numeric(df_.Avg_Vol_Per_3M.str.replace("M","").str.replace(",","")),
            Market_Cap      =  lambda df_:df_.Market_Cap.apply(lambda value: float(value.replace("B","")) if "B" in value else float(value.replace("T","")) * 1000),
            PE_Ratio        =  lambda df_:pd.to_numeric(df_.PE_Ratio.replace("-",np.nan).str.replace(",",""))                                  
            )
        .rename(columns={'Price':'Price_USD',"Volume":"Volume_in_Millions","Market_Cap":"Market_Cap_in_Billions"})
    )
    
    return stocks_df



def clean_and_save_data(input_path, output_path):
    """
    Loads raw stock data, cleans it, and saves the cleaned data.

    """
    try:
        if not os.path.exists(input_path):
            logger.error(f"File not found: {input_path}")
            return
        
        df = pd.read_csv(input_path)
        cleaned_df = clean_yahoo_finance_data(df)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        cleaned_df.to_csv(output_path, index=False)
        logger.info(f"Cleaned data saved to {output_path}")
    except Exception as e:
        logger.error(f"Error in cleaning data: {e}")

if __name__ == "__main__":
    input_file = "data/raw_stocks_details.csv"
    output_file = "data/cleaned_stocks_details.csv"
    clean_and_save_data(input_file, output_file)
