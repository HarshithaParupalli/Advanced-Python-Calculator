import logging
from dotenv import load_dotenv
import os

load_dotenv()

class Logger:
    _instance = None

    @staticmethod
    def get_logger():
        if Logger._instance is None:
            log_level = os.getenv("LOG_LEVEL", "INFO").upper()
            log_file = os.getenv("LOG_FILE", "logs/calculator.log")

            logger = logging.getLogger("CalculatorLogger")
            handler = logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(getattr(logging, log_level))

            Logger._instance = logger

        return Logger._instance
