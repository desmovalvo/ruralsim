#!/usr/bin/python

# system-wide requirements
from uuid import uuid4


class EV:

    """The class that implements the EV"""

    def __init__(self, config, logger):

        """Constructor for the EV class"""

        # logger
        self.logger = logger

        # ev configuration
        self.ev_id = str(uuid4())    
        self.ev_capacity = config["ev_capacity"]
        self.current_charge = config["ev_initial_charge"]
        logger.debug("EV %s succesfully created" % self.ev_id)
