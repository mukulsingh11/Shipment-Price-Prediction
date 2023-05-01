import pandas as pd
from shipment.logger import logging
from shipment.exception import ShipmentException
from shipment.config import mongo_client
import os,sys
import yaml
import numpy as np
import dill 


def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from database : {database_name} and collection : {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f" Found columns : {df.columns}")

        if  ['ID','PQ #','PO / SO #'] in df.columns:
           logging.info(f"Droping columns: 'ID','PQ #','PO / SO #")
           df = df.drop('ID','PQ #', 'PO / SO #', axis = 1)
        logging.info(f'Row and columns in df: {df.shape}')
        return df
    
    except Exception as e:
        raise ShipmentException(e,sys) from e
    
def write_yaml_file(file_path,data:dict):
    try:
      file_dir = os.path.dirname(file_path)
      os.makedirs(file_dir,exist_ok=True)
      with open (file_path , 'w') as file_writer:
        yaml.dump(data,file_writer)
    except Exception as e:
      raise ShipmentException(e,sys)
    
def convert_columns_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    try:
        for column in df.columns:
         if column not in exclude_columns:
            df[column]=df[column].astype('float')
        return df
    except Exception as e:
      raise ShipmentException(e,sys) from e
    

    
