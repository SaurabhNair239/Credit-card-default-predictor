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
from sklearn.metrics import precision_score,accuracy_score
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
                "Logistic Regression": LogisticRegression(),
                "Random Forest":RandomForestClassifier(),
                "Decision Tree": DecisionTreeClassifier(),
                "SVM": SVC(),
                "XGBClassifier": XGBClassifier(),
                "KNN":KNeighborsClassifier()
            }     

            report = evaluation(X_train,y_train,X_test,y_test,model=models)

            report_values = list(report.values())
            report_keys = list(report.keys())

            model_name = report_keys[report_values.index(max(report_values))]

            best_model = models[model_name]

            if max(report_values) < 0.6:
                raise CustomException("No best Model Found")
            
            logging.info("Found best model")

            save_object(file_path=self.model_path.train_model_path,obj_file=best_model)
            

            prediction = best_model.predict(X_test)

            acc = accuracy_score(y_test,prediction)

            return acc 
        except Exception as e:
            raise CustomException(e,sys)
