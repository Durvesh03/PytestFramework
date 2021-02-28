import logging

class LogGen:
    @staticmethod
    def loggens():
        logging.basicConfig(filename="C:\\Users\\durve\\PycharmProjects\\PytestFramework\\Logs\\automation.txt",
                            format = '%(asctime)s: %(levelname)s: %(message)s', datefmt ='%m/%d/%Y %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger




