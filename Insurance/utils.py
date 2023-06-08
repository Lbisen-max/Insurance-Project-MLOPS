
import pandas as pd
import numpy as np
import os
import sys
from Insurance.exceptions import InsuranceException
from Insurance.config import mongo_client
from Insurance.logger import logging


# defining the function so that data vcan read from out mongodb database

def get_collection_as_dataframe(database_name:str,collection_name:str):

    try:
        logging.info(f"Reading data from database:{database_name} and collection : {collection_name}")
        df = pd.DataFrame(mongo_client[database_name][collection_name].find())
        logging.info(f"Find Columns {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Droping columns: _id")
            df = df.drop("_id",axis=1)
        
        logging.info(f"Rows and Columns in df :{df.shape}")
        
        return df


    except Exception as e:
        raise InsuranceException(e,sys)

        
       
                
                

    
        

    

