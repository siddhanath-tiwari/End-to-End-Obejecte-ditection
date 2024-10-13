from signLanguage.logger import logging
import sys
from signLanguage.exception import SignException

# logging.info("Welcome to signLanguage project") # logging at info level

try:
    a = 7 / "9"
    
except Exception as e:
    raise SignException(e, sys) from e
