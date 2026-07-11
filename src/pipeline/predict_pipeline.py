import sys
import os 

import pandas as pd

from src.exception import customexception

from src.utils import load_object
from src.logger import logging

class Pipeline:   
    def __init__(self): 
        pass 

    def predict(self,features):   ## this function is mainly to return the predicted value 
        try:
            model_path = os.path.join("artifacts" , "model.pkl")
            preprocessor_path = os.path.join("artifacts","preprocessor.pkl")
            logging.info("loading the model")
            print("loading model")

            model = load_object(model_path)

            logging.info("loading preprocessor")
            print("loading the preprocessor")

            preprocessor = load_object(preprocessor_path)

            data_transformed = preprocessor.transform(features)

            pred = model.predict(data_transformed)
            
            return pred
        except Exception as e: 
            raise customexception(e , sys)

class customdata: 
    def __init__(self , Contract,tenure,MonthlyCharges,
                 TotalCharges,InternetService,TechSupport,PaymentMethod,Dependents): 
        self.Contract = Contract
        self.InternetService = InternetService
        self.tenure = tenure
        self.MonthlyCharges = MonthlyCharges
        self.TechSupport = TechSupport 
        self.PaymentMethod= PaymentMethod
        self.Dependents = Dependents 
        self.TotalCharges = TotalCharges 

    def get_data_as_dataframe(self): 
        try: 
            features = {
                "Contract" : self.Contract, 
                "InternetService" : self.InternetService, 
                "tenure" : self.tenure, 
                "MonthlyCharges" : self.MonthlyCharges, 
                "TechSupport" : self.TechSupport, 
                "PaymentMethod" : self.PaymentMethod,  
                "Dependents" : self.Dependents, 
                "TotalCharges" : self.TotalCharges
            }
            return pd.DataFrame([features])
        except Exception as e: 
            raise customexception(e , sys)
                
            
        