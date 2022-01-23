from fritzconnection import FritzConnection
from fritzconnection.lib.fritzcall import FritzCall
from fritzconnection.lib.fritzhosts import FritzHosts
from fritzconnection.lib.fritzstatus import FritzStatus

from models.config_model import ConfigurationModel
from modules.database.sqllite import Database


class FritzboxConnect:
    def __init__(self, config: ConfigurationModel):
        address: str = config.connection_address
        username: str = config.connection_username
        password: str = config.connection_password
        port: str = config.connection_port

        if config.features_enable_phone_call_tracking:
            self.__FCALL = FritzCall(address=address, user=username, password=password, port=port, timeout=2.0)
        self.__FCONN = FritzConnection(address=address, user=username, password=password, port=port, timeout=2.0)
        self.__FHOSTS = FritzHosts(address=address, user=username, password=password, port=port, timeout=2.0)
        self.__FSTAT = FritzStatus(address=address, user=username, password=password, port=port, timeout=2.0)
        self.__DB = Database()
        self.__CONFIG = config

        # get info of DSL (WANPPP) or Cable (WANIP)
        if len(self.read_module('WANPPPConnection1', 'GetInfo')) > 0:
            self.__FCONN_INFO = self.read_module('WANPPPConnection1', 'GetInfo')
        else:
            self.__FCONN_INFO = self.read_module('WANIPConnection1', 'GetInfo')

    def config(self):
        return self.__CONFIG

    def call(self):
        return self.__FCALL

    def connection(self) -> FritzConnection:
        return self.__FCONN

    def connection_info(self) -> FritzConnection:
        return self.__FCONN_INFO

    def hosts(self) -> FritzHosts:
        return self.__FHOSTS

    def status(self):
        return self.__FSTAT

    def read_module(self, module: str, action: str):
        try:
            answer = self.connection().call_action(module, action)
        except:
            answer = dict()  # return an empty dict in case of failure
        return answer

    def database(self):
        return self.__DB
