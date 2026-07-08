import logging

import os 
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"  ##this line creates a log file current date and time 07_07_2026_10_30_45.log

log_path = os.path.join(os.getcwd() , "logs" , LOG_FILE)  ### this line creates a folder in the project folder(churn_prediction) by using the LOGS_FILE C:\Users\shaik\Customer_Churn\logs\07_07_2026_10_30_45.log

os.makedirs(os.path.dirname(log_path) , exist_ok = True) ### this line creates the folder in the log path os.path.dirname can remove the log files and place only the folder path so os.makedir create the folder in the project folder 

LOG_FILE_PATH = log_path

logging.basicConfig(
    filename = LOG_FILE_PATH, 
    level = logging.INFO,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__": 
    logging.info("my first log excution")
