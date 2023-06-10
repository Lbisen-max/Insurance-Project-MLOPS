
import pandas as pd
import numpy as np
import os
import sys
from Insurance.exceptions import InsuranceException
from Insurance.config import mongo_client
from Insurance.logger import logging
import dill
import yaml



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
    

def write_yaml_file(file_path,data:dict):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_dir,"w") as file_writer:
            yaml.dump(data,file_writer)
    except Exception as e:
        raise InsuranceException(e,sys)



def convert_columns_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    try:
        for column in df.columns:
            if column not in exclude_columns:
                if df[column].dtype != 'O':
                    df[column] = df[column].astype('float')

        return df
            
    except Exception as e:
        raise InsuranceException(e,sys)


        
       
                
                

    
        

    

