import sys
import numpy as np
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.exception import CustomException
import os
from src.utils import save_object
from sklearn.base import BaseEstimator,TransformerMixin


@dataclass
class DataTranformationSetting:
    preprocess_file_path = os.path.join("artifacts","preprocessor_pipeline.pkl")


class DataTranformation:
    def __init__(self):
        self.data_tranform_setting = DataTranformationSetting()

    def get_data_tranformer(self):
        try:
            numeric_cols = ['LIMIT_BAL','PAY_0','PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2','BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
            'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']
            outlier_cols = ['BILL_AMT1', 'BILL_AMT2','BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
            'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']
            categorical_cols = ['SEX', 'EDUCATION', 'MARRIAGE']
            num_pipeline = Pipeline(
                 steps=[
                ("Standard scaler",StandardScaler())
                 ]   
                )
            logging.info("Pipeline completed for numerical data")
            categorical_pipeline = Pipeline(
                steps=[
                ("OnehotEncoder",OneHotEncoder(sparse=False)),
                ("Standard Scaler",StandardScaler())
                ]
            )
            logging.info("Pipeline completed categorical pipeline")


            numerical_oulier_pipeline = Pipeline(
                steps=[
                ("Onlier removal",OutlierTreatment()),
                ("Simple Imputer",SimpleImputer(strategy="median"))
                ]
            )

            logging.info("Outlier removal treatment done")


            preprocess = ColumnTransformer(
                [
                ("Numerical pipeline",num_pipeline,numeric_cols),
                ("Oulier removal Pipeline",numerical_oulier_pipeline,outlier_cols),
                ("Categorical Pipeline",categorical_pipeline,categorical_cols)
                ]
            )

            logging.info("Combined both the pipelines")
            return preprocess

        except Exception as e:
            raise CustomException(e,sys)
        
    def start_data_tranformation(self,train_path,test_path):
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            logging.info("Loaded Train and Test data")

            logging.info("getting preprocessing steps")

            preprocess_obj = self.get_data_tranformer()

            target_column = "default#payment#next#month"

            input_feature_train = train_data.drop(target_column,axis=1)
            input_feature_test = test_data.drop(target_column,axis=1)

            train_target_feature = train_data[target_column]
            test_target_feature = test_data[target_column]
            
            logging.info("Preprocessing train data")
            train_input_data_preprocessed = preprocess_obj.fit_transform(input_feature_train)

            logging.info("Preprocessing test data")
            test_input_data_preprocessed = preprocess_obj.transform(input_feature_test)

            logging.info("Combining target and input features")

            train_data = np.c_[train_input_data_preprocessed,np.array(train_target_feature)]
            test_data = np.c_[test_input_data_preprocessed,np.array(test_target_feature)]

            logging.info("Preprocessing complete")

            logging.info("Saving Preprocessing pipeline Pickle file")
            save_object(
                    file_path= self.data_tranform_setting.preprocess_file_path,
                    obj_file = preprocess_obj
            )      
            logging.info("Saved Preprocessing pipeline Pickle file")      
            return train_data,test_data,self.data_tranform_setting.preprocess_file_path

        except Exception as e:
            raise CustomException(e,sys)
        

class OutlierTreatment(BaseEstimator,TransformerMixin):
    
    def __init__(self):
        self.lower_bound = []
        self.upper_bound = []

    def outlier_ub_lb(self,X):
        q1 = X.quantile(0.25)
        q3 = X.quantile(0.75)
        iqr = q3-q1
        self.lower_bound.append(q1 - (1.5*iqr))
        self.upper_bound.append(q3 + (1.5*iqr))

    

    def outlier_data_transformer(self,X):
        X.apply(self.outlier_ub_lb)
        for i in range(X.shape[1]):
            copy_data = X.iloc[:,i].copy()
            copy_data[(copy_data < self.lower_bound[i]) & (copy_data > self.upper_bound[i])] = np.nan
            X.iloc[:,i]=copy_data
        return X

               
    def fit_transform(self,X,y=None):
        
        try:
            data_transformed = self.outlier_data_transformer(X)
            return data_transformed
        except Exception as e:
            raise CustomException(e,sys)
        
    def transform(self,X,y=None):
        try:
            for i in range(X.shape[1]):
                copy_data = X.iloc[:,i].copy()
                copy_data[(copy_data < self.lower_bound[i]) & (copy_data > self.upper_bound[i])] = np.nan
                X.iloc[:,i]=copy_data    
            return X
        except Exception as e:
            raise CustomException(e,sys)
        
    def fit(self,X,y=None):
        try:
            self.outlier_data_transformer(X)
            return self
        except Exception as e:
            raise CustomException(e,sys)