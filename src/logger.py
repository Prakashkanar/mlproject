import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")   # directory only, no filename
os.makedirs(logs_dir, exist_ok=True)            # safely creates just the folder

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,  
    filemode="a",                   
    format="[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)d] %(name)s: %(message)s",
    level=logging.INFO,
    force=True,
)

if __name__ == "__main__": 
    logging.info("logging has started")