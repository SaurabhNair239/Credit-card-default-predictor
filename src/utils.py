import os
import sys
from src.logger import logging
import dill
from sklearn.metrics import precision_score,accuracy_score

from src.exception import CustomException 
def save_object(file_path,obj_file):
    try:
        
        directory_path = os.path.dirname(file_path)
        os.makedirs(directory_path,exist_ok=True)
        with open(file=file_path, mode="wb") as path:
            dill.dump(obj_file,path)
    except Exception as e:
        raise CustomException(e,sys)

def evaluation(X_train,y_train,X_test,y_test,model):
    try:
        accuracy_dict = {}
        for i in model.keys():
            model = model[i]
            model.fit(X_train,y_train)
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            
            # train_precision = precision_score(y_train,y_train_pred)
            # test_precision = precision_score(y_test,y_test_pred)

            train_acc = accuracy_score(y_train,y_train_pred)
            test_acc = accuracy_score(y_test,y_test_pred)

            accuracy_dict[i] = test_acc

            return accuracy_dict

    except Exception as e:
        raise CustomException(e,sys)