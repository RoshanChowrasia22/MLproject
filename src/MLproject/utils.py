import os
import sys
from src.MLproject.exception import CustomException
from src.MLproject.logger import logging 
import pandas as pd
import pymysql 
from dotenv import load_dotenv
load_dotenv()

host=os.getenv("host")
user=os.getenv("usr")
password=os.getenv("password")
df=os.getnev("db")

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
