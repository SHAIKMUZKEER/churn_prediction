import os 
import sys 
import numpy as np 
import pandas as pd 

import dill 

from src.exception import customexception
from src.logger import logging
from sklearn.metrics import f1_score,classification_report


def save_object(file_path , obj): 
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path , exist_ok = True)

        with open(file_path , "wb" ) as file_obj:
            dill.dump(obj , file_obj)
    except Exception as e: 
        raise customexception(e,sys) 
    

def evaluate_models(x_train, x_test , y_train , y_test , models):
    try:
        report = {}

        for i in range(len(list(models.values()))):

            model = list(models.values())[i]

            # param = list(params.values())[i]

            # grid = GridSearchCV(model , param , cv = 4 , n_jobs = -1)

            # grid.fit(x_train,y_train)

            # model.set_params(**grid.best_params_)

            model.fit(x_train,y_train)

            y_pred = model.predict(x_test)

            f1 = f1_score(y_test , y_pred)
  

            report[list(models.keys())[i]] = f1


        return report

    except Exception as e : 
        raise customexception(e, sys)


def load_object(file_path): 
    try: 
        with open(file_path , "rb") as file_obj: 
            return dill.load(file_obj)
    except Exception as e: 
        raise customexception(e , sys)
