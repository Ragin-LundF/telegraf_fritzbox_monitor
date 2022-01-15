from models.general.fritz_status_model import FritzboxStatusModel
from modules.fritz_connect import FritzboxConnect


class FritzboxConnectStatus:
    def __init__(self, fc: FritzboxConnect):
        self.__FC_STATUS = fc.status()
        self.__FC_CONN_INFO = fc.connection_info()

    def stats(self) -> FritzboxStatusModel:
        general_model = FritzboxStatusModel(
            uptime=self.uptime(),
            connection_status=self.connection_status(),
            last_error=self.last_connection_error()
        )

        return general_model

    def uptime(self) -> int:
        return self.__FC_STATUS.device_uptime

    def connection_status(self) -> str:
        return self.__FC_CONN_INFO['NewConnectionStatus']

    def last_connection_error(self):
        return self.__FC_CONN_INFO['NewLastConnectionError']
