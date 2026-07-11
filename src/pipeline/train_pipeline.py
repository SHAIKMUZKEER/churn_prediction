from src.components.data_ingestion import data_ingestion
from src.components.data_transformation import datatranformation
from src.components.model_trainer import ModelTrainer 

from src.logger import logging 

if __name__ == "__main__":
    data_ingestion_obj = data_ingestion()

    train_data_path , test_data_path = data_ingestion_obj.initiate_data_ingestion()

    datatransformation_obj = datatranformation()

    train_data , test_data , _ = datatransformation_obj.initiate_data_transformation(train_data_path , test_data_path)

    model_trainer_obj = ModelTrainer()

    f1_score , report = model_trainer_obj.initiate_model_trainer(train_data , test_data)

    logging.info("trainer_pipeline is completed")

    print("f1 score : " , f1_score)
    print("report : " , report)


