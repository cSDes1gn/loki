import os
import time
import logging
import logging.config
from pathlib import Path
from envyaml import EnvYAML
from client.logs.formatter import pformat


def logging_handler(config_path: Path) -> None:
    """
    Configure monitor logger using dict config and set the logging path
    :param config_path: path to log config
    :type config_path: Path
    """
    # bind logging to config file
    # verify path existance before initializing logger file configuration
    try:
        # load config from .yaml
        env = EnvYAML(config_path).export()
        logging.info("Parsed logger config:%s", pformat(env))
        logging.config.dictConfig(env)  # type: ignore
        logging.info('Configuring logger using dict config')
    except ValueError as exc:
        logging.exception(
            "Logging configuration failed due to missing environment variables: %s", exc)
    except FileNotFoundError:
        logging.exception(
            "Logging config file not found in expected absolute path: {}".format(config_path))
    else:
        logging.info("Logging configuration successful.")


logging_handler(
    config_path=Path(__file__).parent.joinpath("logs/config.yaml")
)
_log = logging.getLogger(__name__)

while True:
    _log.debug("debug log")
    _log.info("information log")
    _log.warning("warning log")
    _log.error("error log")
    _log.exception("exception log")
    _log.critical("critical log")
    time.sleep(1)
