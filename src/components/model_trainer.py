import os
import sys
from dataclasses import dataclass
from imblearn.over_sampling import SMOTE

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression 
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier

from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import confusion_matrix , classification_report ,f1_score
from src.exception import customexception
from src.logger import logging

from imblearn.over_sampling import SMOTE
from src.utils import save_object,evaluate_models


@dataclass 

class modeltrainerconfigure: 
    model_trainer_path = os.path.join("artifacts" ,"model.pkl")


class ModelTrainer: 
    def __init__(self): 
        self.model_trainer_config = modeltrainerconfigure()

    def initiate_model_trainer(self , train_data , test_data): 
        logging.info("entered into the model trainer function")
        try:
            x_train = train_data[:,:-1]
            x_test = test_data[: , :-1]
            y_train = train_data[:,-1]
            y_test = test_data[:,-1]

            models = {
                "RandomForestClassifier" : RandomForestClassifier(n_estimators = 600 ,criterion='gini', max_depth = 7 , min_samples_split = 10 , min_samples_leaf = 5 ,random_state = 42 , class_weight = "balanced")
            }
            # models = {
            #     "LogisticRegression" : LogisticRegression(), 
            #     "SVC" : SVC(),
            #     "xgboost" : XGBClassifier(), 
            #     "RandomForestClassifier" : RandomForestClassifier(), 
            #     "GradientBoostingClassifier" : GradientBoostingClassifier(),
            #     "KNeighborsClassifier" : KNeighborsClassifier(), 
            #     "DecisionTreeClassifier" : DecisionTreeClassifier()
            # }
            # params = {
            #     "LogisticRegression": {
            #             "C": [0.01, 0.1, 1, 10],
            #             "penalty": ["l2"],
            #             "solver": ["lbfgs", "liblinear"],
            #             "max_iter": [500, 1000]
            #         },
                
            #         "SVC": {
            #             "C": [0.1, 1, 10],
            #             "kernel": ["linear", "rbf"],
            #             "gamma": ["scale", "auto"]
            #         },
                
            #         "xgboost": {
            #             "n_estimators": [100, 200, 300],
            #             "max_depth": [3, 5, 7],
            #             "learning_rate": [0.01, 0.1, 0.2],
            #             "subsample": [0.8, 1.0],
            #             "colsample_bytree": [0.8, 1.0]
            #         },
                
            #         "RandomForestClassifier": {
            #             "n_estimators": [100, 200, 300],
            #             "max_depth": [None, 10, 20],
            #             "min_samples_split": [2, 5, 10],
            #             "min_samples_leaf": [1, 2, 4],
            #             "max_features": ["sqrt", "log2"]
            #         },
                
            #         "GradientBoostingClassifier": {
            #             "n_estimators": [100, 200],
            #             "learning_rate": [0.01, 0.1, 0.2],
            #             "max_depth": [3, 5],
            #             "subsample": [0.8, 1.0]
            #         },
                
            #         "KNeighborsClassifier": {
            #             "n_neighbors": [3, 5, 7, 9],
            #             "weights": ["uniform", "distance"],
            #             "metric": ["euclidean", "manhattan"]
            #         },
                
            #         "DecisionTreeClassifer": {
            #             "criterion": ["gini", "entropy"],
            #             "max_depth": [None, 5, 10, 20],
            #             "min_samples_split": [2, 5, 10],
            #             "min_samples_leaf": [1, 2, 4],
            #             "max_features": [None, "sqrt", "log2"]
            #         }
            # }
           

            model_report:dict = evaluate_models(x_train,x_test , y_train , y_test , models)

            best_score =  max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_score)]

            best_model = models[best_model_name]


            if best_score<0.6:
                logging.info(f"Best found model on both training and testing dataset")
                raise customexception("No best model found")

            logging.info("best model is searched")
            best_model.fit(x_train, y_train)

            save_object(
                file_path=self.model_trainer_config.model_trainer_path,obj=best_model
            )

            logging.info("model training is over")

            y_pred = best_model.predict(x_test)
            
            f1 = f1_score(y_test , y_pred)
            report = classification_report(y_test , y_pred)

            return f1 , report
            

        except Exception as e:
            raise customexception(e,sys)

    


