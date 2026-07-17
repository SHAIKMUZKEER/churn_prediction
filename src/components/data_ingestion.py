import os
import sys
from src.exception import customexception 
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split

from src.components.data_transformation import data_transformation_configure
from src.components.data_transformation import datatranformation

from src.components.model_trainer import modeltrainerconfigure
from src.components.model_trainer import ModelTrainer

class Dataconfigure: 
    def __init__(self): 
        self.train_data_path = os.path.join("artifacts" , "train.csv")
        self.test_data_path = os.path.join("artifacts" , "test.csv")
        self.raw_data_path = os.path.join("artifacts" , "data.csv")

class data_ingestion(Dataconfigure): 
    def initiate_data_ingestion(self): 
        logging.info("entered the data ingestion function")

        try: 
            df=pd.read_csv('notebook\data\churn_data.csv')

            logging.info("data is readed in dataframe")

            os.makedirs(os.path.dirname(self.train_data_path) , exist_ok = True)

            df.to_csv(self.raw_data_path , index = False , header = True)

            train_data , test_data = train_test_split(df , test_size = 0.2 , random_state= 42)

            train_data.to_csv(self.train_data_path , index = False , header = True)

            test_data.to_csv(self.test_data_path , index = False , header = True)

            logging.info("data has succesfully injected")

            return self.train_data_path , self.test_data_path
        except Exception as e: 
            raise customexception(e , sys)


if __name__ == "__main__":
    obj = data_ingestion()
    train_path , test_path = obj.initiate_data_ingestion()

    obj_data_transform = datatranformation()
    train_data , test_data ,_ = obj_data_transform.initiate_data_transformation(train_path, test_path)

    obj_modeltrainer = ModelTrainer()
    f1 , report = obj_modeltrainer.initiate_model_trainer(train_data , test_data)
    print(f1)

