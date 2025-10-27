from src.MLproject import logger
from src.MLproject.exception import CustomException
import sys
from src.MLproject.components.data_ingestion import DataIngestion
from src.MLproject.components.data_ingestion import DataIngestionConfig

from src.MLproject.components.data_transformation import DataTransformationConfig,DataTransformation
from src.MLproject.components.model_trainer import ModelTrainerConfig,ModelTrainer


if __name__=="__main__":
    logger.logging.info("The execution has started")

    try:
        # data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        # data_transformation_config=DataIngestionConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_path=train_data_path,test_path=test_data_path)

        model_trainer=ModelTrainer()
        R2_score=model_trainer.inititate_model_trainer(train_array=train_arr,test_array=test_arr)

        print(f"Hola the R2 score is {R2_score}")
    except Exception as e:
        logger.logging.info("Custom Exception")
        raise CustomException(e,sys)