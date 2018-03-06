import logging
import inspect


def customLogger(logLevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", "a")
    fileHandler.setLevel(logLevel)

    logFormat = "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
    dateFormat = "%Y-%m-%d %I:%M:%S"
    formatter = logging.Formatter(logFormat, dateFormat)

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
