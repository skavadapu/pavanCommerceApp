import logging


class LogGen:
    @staticmethod
    def loggen():
        fileHandler = logging.FileHandler('.\\Logs\\automation.log')
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        fileHandler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
