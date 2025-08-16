from src.MLproject import logger
from src.MLproject.exception import CustomException
import sys
from src.MLproject.components.data_ingestion import DataIngestion
from src.MLproject.components.data_ingestion import DataIngestionConfig

if __name__=="__main__":
    logger.logging.info("The execution has started")

    try:
        # data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logger.logging.info("Custom Exception")
        raise CustomException(e,sys)