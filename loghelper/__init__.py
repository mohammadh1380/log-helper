import logging
import sys
import datetime as dt
from logging import Logger
from logging.handlers import TimedRotatingFileHandler

DEFAULT_LOG_FORMAT = "%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d %(funcName)s] %(message)s" \
    # " - PID:%(process)d/%(processName)s - TID:%(thread)d/%(threadName)s"
# - %(name)s
# TODO: add extras fields (e.g. username, client_ip, request_body), implement this with customConfig by the user (dev)
#


class CommonLogger(Logger):
    def __init__(self, name=None, log_file=None,
                 log_format=DEFAULT_LOG_FORMAT,
                 *args, **kwargs
                 ):
        self.formatter = logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S%z')
        self.log_file = log_file

        Logger.__init__(self, name, *args, **kwargs)

        self.addHandler(self.get_console_handler())

        if log_file:
            self.addHandler(self.get_file_handler())

        # it is not required to propagate to the parent loggers
        self.propagate = False

    def get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    def get_file_handler(self):
        # Set default rotation to 3 days, change as you need
        file_handler = TimedRotatingFileHandler(self.log_file, when="D", interval=3)
        file_handler.setFormatter(self.formatter)
        return file_handler


class CustomFormatter(logging.Formatter):
    converter = dt.datetime.fromtimestamp

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%Y-%m-%d %H:%M:%S")
            s = "%s.%03d" % (t, record.msecs)
        return s
