import time
import random
import logging

class Client:
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    def start(self):
        while True:
            self.log_debug()
            self.log_info()
            self.log_warning()
            self.log_error()

    def log_info(self):
        if bool(random.getrandbits(1)):
            self._logger.info("this is an info log")
        time.sleep(random.randint(1, 5))

    def log_debug(self):
        if bool(random.getrandbits(1)):
            self._logger.debug("this is a debug log")
        time.sleep(random.randint(1, 5))

    def log_warning(self):
        if bool(random.getrandbits(1)):
            self._logger.warning("this is a warning log")
        time.sleep(random.randint(1, 5))

    def log_error(self):
        if bool(random.getrandbits(1)):
            self._logger.error("this is an error log")
        time.sleep(random.randint(1, 5))
