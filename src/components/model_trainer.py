from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
import sys
from src.utils import evaluation
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import os
from src.utils import save_object

@dataclass
class model_training_settings:
    train_model_path = os.path.join("artifacts","model.pkl")


class model_trainer:
    def __init__(self):
        self.model_path = model_training_settings()

    def training_model(self,train_arr,test_arr,preprocessor_path):
        try:
            logging.info("Splitting input and target variable")
            X_train,y_train,X_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )       
            models = {
                "Random Forest":RandomForestClassifier(),
                "Decision Tree": DecisionTreeClassifier(),
                # "SVM": SVC(),
                "XGBClassifier": XGBClassifier(),
                "KNN":KNeighborsClassifier()
            }     
            

            hyper_parameter = {

                "Random Forest":{
                    'criterion': ['gini','entropy'],
                    'max_depth':[10,20,30],
                    'min_samples_split': [0.2,0.3,0.5],
                    'n_estimators':[100,150,200]
                },
                
                "Decision Tree":{
                'criterion': ['gini','entropy'],
                'splitter': ['random','best'],
                'max_depth': [10,30,20],
                'min_samples_split': [0.2,0.3,0.5]
                },

            #     "SVM":{
            #     'C': [0.1, 1, 10 ], 
            #   'gamma': [1, 0.1, 0.01],
            #     },

                "XGBClassifier":{
                'learning_rate':[0.1,0.01,0.001],
                'max_depth':[3,5,7,9],
                'n_estimators': [4,10,20,50,150,140] 
                },

                "KNN":{
                'n_neighbors': list(range(1,15,2))
                }

            }

            report = evaluation(X_train,y_train,X_test,y_test,model=models,parameters=hyper_parameter)


            report_acc = [i[0] for i in report.values()]
            model_data = [i[1] for i in report.values()]
            best_model = model_data[report_acc.index(max(report_acc))]
            report_keys = [i for i in report.keys()]
            model_name = report_keys[report_acc.index(max(report_acc))]
            print("Best Model: ",model_name)
            if max(report_acc) < 0.6:
                raise CustomException("No best Model Found")
            
            logging.info("Found best model")

            save_object(file_path=self.model_path.train_model_path,obj_file=best_model)
            

            prediction = best_model.predict(X_test)

            acc = accuracy_score(y_test,prediction)

            return acc 
        except Exception as e:
            raise CustomException(e,sys)
