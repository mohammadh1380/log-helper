import logging
from loghelper import CommonLogger

# Tests
if __name__ == '__main__':
    # Test console logger with file handler
    # USE THE LOGGER LIKE THIS
    logger = CommonLogger(__name__, log_file='../logs/app.log', level=logging.DEBUG)
    logger.info("Test console logger with file handler")
    logger.warning("Test console logger with file handler", extra={'user': 'SomeUser'})

    # Test console-only logger
    console_logger = CommonLogger(__name__, level=logging.DEBUG)
    console_logger.debug("Test console message")

    # Test logging inside functions
    def test_func():
        func_logger = CommonLogger(__name__)
        func_logger.error("Logging mock_exception inside function")
        logger.warning("Reused the logger with file handler from outer scope")


    test_func()

    from tests.test_some_module import test_func as test_func_from_another_file

    test_func_from_another_file()

    # log records with a custom format with extra fields
    custom_logger = CommonLogger(__name__, level=logging.DEBUG,
                                 log_format="%(asctime)s %(levelname)-8s %(name)s "
                                            "[%(filename)s:%(lineno)d %(funcName)s] %(clientip)s %(message)s")
    custom_logger.info("User login", extra={'clientip': '127.0.0.1'})
