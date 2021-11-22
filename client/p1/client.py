import time
import logging

class Client:
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)

    def start(self):
        while True:
            self._logger.debug("debug log")
            self._logger.info("information log")
            self._logger.warning("warning log")
            self._logger.error("error log")
            self._logger.critical("critical log")
            time.sleep(5)
