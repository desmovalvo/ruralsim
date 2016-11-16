#!/usr/bin/python

# system-wide requirements
from uuid import uuid4


class EVSE:

    """The class that implements the EVSE"""

    def __init__(self, config, logger):

        """Constructor for the EVSE class"""

        # logger
        self.logger = logger

        # evse configuration
        self.evse_id = str(uuid4())
        self.storage_capacity = config["storage_capacity"]
        self.current_charge = config["storage_initial_charge"]
        self.policy = config["storage_policy"]
        self.network_power = config["network_power"]
        self.storage_power = config["storage_power"]
        logger.debug("EVSE %s succesfully created" % self.evse_id)
