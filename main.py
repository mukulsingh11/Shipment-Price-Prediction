from shipment.logger import logging
from shipment.exception import ShipmentException
import sys,os
from shipment.utils import get_collection_as_dataframe
from shipment.entity import config_entity
from shipment.components.data_ingestion import DataIngestion

print(__name__)
if __name__=="__main__":

    try:
        training_pipeline_config  = config_entity.TrainingPipelineConfig()
        data_ingestion_config =config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        print(data_ingestion.initiate_data_ingestion())

    except Exception as e:
        print(e)
       

