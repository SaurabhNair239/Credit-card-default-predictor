import os
import sys
from sklearn.model_selection import GridSearchCV
from src.logger import logging
import dill
from sklearn.metrics import precision_score,accuracy_score
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from src.exception import CustomException 
def save_object(file_path,obj_file):
    try:
        
        directory_path = os.path.dirname(file_path)
        os.makedirs(directory_path,exist_ok=True)
        with open(file=file_path, mode="wb") as path:
            dill.dump(obj_file,path)
    except Exception as e:
        raise CustomException(e,sys)

def evaluation(X_train,y_train,X_test,y_test,model,parameters):
    try:
        accuracy_dict = {}
        over_sampler = SMOTE()
        X_smote_data,y_smote_data = over_sampler.fit_resample(X_train,y_train)
        for i in model.keys():
            model_obj = model[i]
            print(i)
            parameter = parameters[i]
            grid_model  = GridSearchCV(model_obj,param_grid=parameter,cv=10,n_jobs=-1,refit=False,scoring='accuracy')
            grid_model.fit(X_smote_data,y_smote_data)
            model_obj.set_params(**grid_model.best_params_)
            model_obj.fit(X_train,y_train)
            y_train_pred = model_obj.predict(X_train)

            y_test_pred = model_obj.predict(X_test)
            
            # train_precision = precision_score(y_train,y_train_pred)
            # test_precision = precision_score(y_test,y_test_pred)

            train_acc = accuracy_score(y_train,y_train_pred)
            test_acc = accuracy_score(y_test,y_test_pred)

            accuracy_dict[i] = [test_acc]
            print(accuracy_dict[i])
            accuracy_dict[i].append(model_obj)

        return accuracy_dict

    except Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path):
        try:
            with open(file=file_path,mode="rb") as f_obj:
                return dill.load(f_obj)
        except Exception as e:
            raise CustomException(e,sys)