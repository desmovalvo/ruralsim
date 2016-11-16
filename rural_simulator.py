#!/usr/bin/python

# system-wide requirements
import logging

# local requirements
from lib.Configuration import *
from lib.EVSE import *


# main
if __name__ == "__main__":
    
    # read the configuration file
    c = Configuration("settings.conf")
    logger_conf = c.read_logger_config()
    evse_conf = c.read_evse_config()

    # create an instance of the logger
    logger = logging.getLogger('ruralSIM')
    logger.setLevel(logger_conf["log_level"])
    ch = logging.StreamHandler()
    ch.setLevel(logger_conf["log_level"])
    formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.debug("Simulator configuration completed!")

    # create the EVSEs
    evses = []
    logger.debug("Creating %s EVSEs" % evse_conf["evse_number"])
    for evse in xrange(evse_conf["evse_number"]):

        # create an instance of the EVSE class for each evse
        evses.append(EVSE(evse_conf, logger))
