import logging

from loghelper import CommonLogger

logger = logging.getLogger(__name__)

logger.info("info")
logger.error("error")
logger.critical("critical")
logger.warning("warning")
logger.debug("debug")

common_logger = CommonLogger()
common_logger.info("Some log")
