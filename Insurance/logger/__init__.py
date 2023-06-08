import logging
from datetime import datetime
import os

LOG_DIR = "Insurance_log" # defining the log folder

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}" # Defining the date time

LOG_FILE_NAME = f"log_ {CURRENT_TIME_STAMP}.log" 

os.makedirs(LOG_DIR,exist_ok=True) # if file is not exist then this will create the file

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    # filemode="w", # file mode as write mode
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.DEBUG,
)