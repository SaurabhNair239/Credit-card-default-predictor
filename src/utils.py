import os
import sys
from src.logger import logging
import dill

from src.exception import CustomException 
def save_object(file_path,obj_file):
    try:
        
        directory_path = os.path.dirname(file_path)
        os.makedirs(directory_path,exist_ok=True)
        with open(file=file_path, mode="wb") as path:
            dill.dump(obj_file,path)
    except Exception as e:
        raise CustomException(e,sys)