import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
import pyodbc
from dataclasses import dataclass

@dataclass
class DataIngestionPaths:
    train_path = os.path.join("artifacts","train.csv")
    test_path = os.path.join("artifacts","test.csv")
    raw_path = os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_path = DataIngestionPaths()

    def start_ingestion_data(self):
        logging.info("Started Data ingestion method")
        try:
            #data = pd.read_csv("notebook/data/UCI_Credit_Card.csv")
            server = "studentpractice.database.windows.net"
            db_name = "credit_card_defaulter"
            username= "Saurabh"
            password = "C50keshavkunj"
            driver= '{ODBC Driver 17 for SQL Server}'
            conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + db_name + ';UID=' + username + ';PWD=' + password)
            
            # cur = conn.cursor()
            # cur.execute("select * from [dbo].[data_1$]")
            # data = cur.featchall()
            data = pd.read_sql("select * from [dbo].[data_1$]",conn)
                        
            logging.info("Loaded data as DF")

            os.makedirs(os.path.dirname(self.ingestion_path.test_path),exist_ok=True)

            data.to_csv(self.ingestion_path.raw_path,index=False,header=True)

            logging.info("Initiated Train Test Split")

            train_set,test_set = train_test_split(data,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_path.train_path,index=False,header=True)

            test_set.to_csv(self.ingestion_path.test_path,index=False,header=True)

            logging.info("Completed Data Ingestion")

            return (
                self.ingestion_path.train_path,
                self.ingestion_path.test_path
            )
        except Exception as e :
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    data_injestion_obj = DataIngestion()
    data_injestion_obj.start_ingestion_data()