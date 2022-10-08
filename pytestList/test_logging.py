import logging


# first create an object for logging and pass __name__ as parameter for the testfile name to be rendered in html report


def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # filehandler object determines what format and file to print in

    logger.setLevel(logging.DEBUG) # note this can be set as INFO or DEBUG
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has occurred")
    logger.critical("Critical issue")
