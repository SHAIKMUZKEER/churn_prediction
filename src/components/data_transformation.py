import sys 
import os
import numpy as np 
import pandas as pd

from dataclasses import dataclass 
from sklearn.compose import ColumnTransformer

from sklearn.impute import SimpleImputer 
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import OneHotEncoder , StandardScaler
from src.exception import customexception
from src.logger import logging 

from src.utils import save_object
from imblearn.over_sampling import SMOTE

@dataclass 
class data_transformation_configure: 
    preprocessor_file_path = os.path.join("artifacts" , "preprocessor.pkl")

class datatranformation: 
    def __init__(self): 
        self.preprocessor_path =  data_transformation_configure()

    def get_data_transformation(self): 
        logging.info("entered in the transformation function")

        try: 

            numeric_features = ["tenure","MonthlyCharges","TotalCharges"]

            categorical_features = ['Contract', 'InternetService', 'TechSupport', 'PaymentMethod','Dependents']

            num_pipeline = Pipeline(
                steps = [
                    ("imputer" , SimpleImputer(strategy = "median")), 
                    ("scaler" , StandardScaler())
                ]
            )

            categorical_pipeline = Pipeline(
                steps = [
                        ("imputer_caterical" , SimpleImputer(strategy = "most_frequent")),
                        ("onehot" , OneHotEncoder(handle_unknown = "ignore" , sparse_output = False)),
                    ]
            )

            preprocessor = ColumnTransformer(
                [
                        ("numerical_pipeline" , num_pipeline ,numeric_features),
                        ("categorical_process" , categorical_pipeline ,categorical_features)
                    ]
            )

            logging.info("transformation processor is ready")

            return preprocessor
        except Exception as e:
            raise customexception(e , sys)

    def initiate_data_transformation(self , train_path, test_path):
        logging.info("entered into data transformation function to perform the preprocessing")

        try: 
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessor_obj = self.get_data_transformation()

            features = ["tenure","MonthlyCharges","TotalCharges",'Contract', 'InternetService', 'TechSupport', 'PaymentMethod','Dependents']
            
            train_data["TotalCharges"] = pd.to_numeric(train_data["TotalCharges"] , errors = "coerce")
            test_data["TotalCharges"] = pd.to_numeric(test_data["TotalCharges"] , errors = "coerce")

            train_data["TotalCharges"].fillna(train_data["TotalCharges"].mean)
            test_data["TotalCharges"].fillna(test_data["TotalCharges"].mean)


            input_train_data = train_data[features]
            train_data["Churn"] = train_data["Churn"].map({"Yes" : 1 , "No" : 0})
            target_train_data = train_data["Churn"]

            input_test_data = test_data[features]
            test_data["Churn"] = test_data["Churn"].map({"Yes" : 1 , "No" : 0})
            target_test_data = test_data["Churn"]

            
            sm = SMOTE(random_state= 42)


            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessor_obj.fit_transform(input_train_data)
            input_feature_test_arr=preprocessor_obj.transform(input_test_data)

            

            input_feature_train_arr , target_train_data = sm.fit_resample(input_feature_train_arr , target_train_data)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_train_data)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_test_data)]

            logging.info(f"Saved preprocessing object.")

            save_object(file_path = self.preprocessor_path.preprocessor_file_path , obj = preprocessor_obj)

            return (
                train_arr, 
                test_arr,
                self.preprocessor_path.preprocessor_file_path
            )

              
        except Exception as e: 
            raise customexception(e , sys)
         


