import logging
import os

from datetime import datetime 

LOG_FILE=f"{datetime.now().strftime('%m_%d%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,             # path to your log file
    level=logging.INFO,                 # log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",  
    datefmt="%Y-%m-%d %H:%M:%S"         # timestamp format
)