import logging
from loghelper import CommonLogger

# Tests
if __name__ == '__main__':
    # Test console logger with file handler
    # USE THE LOGGER LIKE THIS
    logger = CommonLogger(log_file='../logs/app.log', level=logging.DEBUG)
    logger.info("Test console logger with file handler")
    logger.warning("Test console logger with file handler", extra={'user': 'SomeUser'})

    # Test console-only logger
    console_logger = CommonLogger(name="a.b", level=logging.DEBUG)
    console_logger.debug("Test console message")

    # Test logging inside functions
    def test_func():
        func_logger = CommonLogger(__name__)
        func_logger.error("Logging mock_exception inside function")
        logger.warning("Reused the logger with file handler from outer scope")

    test_func()
