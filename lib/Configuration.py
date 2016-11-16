#!/usr/bin/python

# system-wide requirements
import ConfigParser

class Configuration:

    # constructor
    def __init__(self, config_file):

        """Constructor for the Configuration class"""

        # instance of the ConfigParser
        self.cp = ConfigParser.ConfigParser()
        self.cp.readfp(open(config_file))
    

    # logger config reader
    def read_logger_config(self):
        
        """Reads the configuration of the logger"""
        conf = {}
        conf["log_level"] = self.cp.getint("Logger", "level")
        return conf


    # EVSE config reader
    def read_evse_config(self):
        
        """Reads the configuration of an EVSE"""

        # EVSE configuration
        conf = {}
        conf["evse_number"] = self.cp.getint("EVSE", "evse_number")
        conf["storage_capacity"] = self.cp.getint("EVSE", "storage_capacity")
        conf["storage_initial_charge"] = self.cp.getint("EVSE", "storage_initial_charge")
        conf["storage_policy"] = self.cp.get("EVSE", "storage_policy")
        conf["network_power"] = self.cp.getint("EVSE", "network_power")
        conf["storage_power"] = self.cp.getint("EVSE", "storage_power")
        return conf


    # EV config reader
    def read_ev_config(self):
        
        """Reads the configuration of an EV"""

        # EV configuration
        conf = {}
        conf["ev_number"] = self.cp.getint("EV", "ev_number")
        conf["ev_capacity"] = self.cp.getint("EV", "ev_capacity")
        conf["ev_initial_charge"] = self.cp.getint("EV", "ev_initial_charge")
        return conf
