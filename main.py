from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_enitiy import DataIngestionConfig
from networksecurity.entity.config_enitiy import TrainingPipelineConfig
from networksecurity.constant import training_pipeline
from networksecurity.entity.artifact_entity import DataIngestionArtifact
from networksecurity.logging.logger import logging as logger
from networksecurity.components.data_transformation import DataTransformation,DataTransformationConfig
from networksecurity.components.model_trainer import ModelTrainer,ModelTrainerArtifact,ModelTrainerConfig

from networksecurity.components.data_validation import DataValidation,DataValidationConfig,DataValidationArtifact

import os
import sys  

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
     
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
    
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logger.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logger.info("data Validation Completed")

        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logger.info("data Transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logger.info("data Transformation completed")

        logger.info("Model Training sstared")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logger.info("Model Training artifact created")

    except Exception as e:
        raise NetworkSecurityException(e, sys)
