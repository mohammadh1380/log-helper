import logging
from log_helper import CommonLogger

logger = logging.getLogger(__name__)

print("Logger", logger.name, "level:", logger.level)
logger.info("info")
logger.error("error")


def test_func():
    logger.critical("critical")
    logger.warning("warning")
    logger.debug("debug")


test_func()

common_logger = CommonLogger()
common_logger.info("Some log")
