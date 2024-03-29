import os,sys
from shipment.exception import ShipmentException
from shipment.logger import logging
from datetime import datetime

FILE_NAME = 'shipment.csv'
TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'

class TrainingPipelineConfig:

    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),'artifact',f"{datetime.now().strftime('%m%d%y__%H%M%S')}")
        except Exception as e:
            raise ShipmentException(e,sys) from e
        
class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):

        try:
            self.database_name = 'Supply Chain'
            self.collection_name = 'shipment'
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,'data_ingestion')
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,'feature_store',FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,'dataset',TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,'dataset',TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception as e:
            raise ShipmentException(e,sys) from e
        
    def to_dict(self,)->dict:

        try:
            self.__dict__
        except Exception as e:
            raise ShipmentException(e,sys)
        
        
