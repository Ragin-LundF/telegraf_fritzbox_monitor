import logging
from typing import Any

import hiyapyco

from models.config_model import ConfigurationModel


class Configuration:
    def __init__(self):
        self.__config_yaml = self.__load_config()
        self.__config = ConfigurationModel()
        self.__config.set_connection_username(self.__connection_fritz_username())
        self.__config.set_connection_password(self.__connection_fritz_password())
        self.__config.set_connection_port(self.__connection_fritz_port())
        self.__config.set_defaults_database(self.__default_database())
        self.__config.set_defaults_phone_days(self.__defaults_phone_days())
        self.__config.set_defaults_phone_days_kept(self.__defaults_phone_days_kept())
        self.__config.set_features_enable_phone_call_tracking(self.__features_phone_call_tracking())

    def get(self):
        return self.__config

    def __load_config(self) -> Any:
        return hiyapyco.load('config.yaml', 'config_custom.yaml', method=hiyapyco.METHOD_MERGE, interpolate=True,
                             failonmissingfiles=False, loglevelmissingfiles=logging.DEBUG)

    def __connection_fritz_username(self):
        return self.__config_yaml.get('connection')['fritzbox_username']

    def __connection_fritz_password(self):
        return self.__config_yaml.get('connection')['fritzbox_password']

    def __connection_fritz_port(self):
        return self.__config_yaml.get('connection')['fritzbox_port']

    def __default_database(self):
        return self.__config_yaml.get('defaults')['influx_database']

    def __defaults_phone_days(self):
        return self.__config_yaml.get('defaults')['fritzbox_phone_call_days']

    def __defaults_phone_days_kept(self):
        return self.__config_yaml.get('defaults')['fritzbox_phone_days_local_storage']

    def __features_phone_call_tracking(self) -> bool:
        return self.__config_yaml.get('features')['enable_phone_call_tracking']
