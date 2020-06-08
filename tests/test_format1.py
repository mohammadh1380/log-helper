from loghelper import CommonLogger


def test_func():
    common_logger = CommonLogger(__name__)
    common_logger.info("Some log")


if __name__ == '__main__':
    test_func()
