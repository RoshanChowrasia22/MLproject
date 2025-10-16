import os
import sys
from src.MLproject.exception import CustomException
from src.MLproject.logger import logging 
import pandas as pd
import pymysql 
from dotenv import load_dotenv
import pickle
load_dotenv()

host=os.getenv("host")
user=os.getenv("usr")
password=os.getenv("password")
df=os.getenv("db")

# Generic fucntionality 

def read_sql_data():
    logging.info("Reading SQL data base started")
    try:
        mydb=pymysql.connect(host=host,user=user,password=password,db=db)
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head(10))
        return df
        
    except Execution as ex:
        raise CustomException(ex,sys)

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)