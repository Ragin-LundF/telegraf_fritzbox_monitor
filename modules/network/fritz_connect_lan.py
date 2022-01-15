from models.network.fritzbox_lan_model import FritzboxLANModel
from modules.fritz_connect import FritzboxConnect


class FritzboxConnectLAN:
    def __init__(self, fc: FritzboxConnect):
        self.__LAN_STATS = fc.read_module('LANEthernetInterfaceConfig1', 'GetStatistics')

    def stats(self) -> FritzboxLANModel:
        lan_model = FritzboxLANModel(
            bytes_sent=self.bytes_sent(),
            bytes_received=self.bytes_received(),
            packets_sent=self.packets_sent(),
            packets_received=self.packets_received()
        )

        return lan_model

    def bytes_sent(self) -> int:
        return self.__LAN_STATS.get('NewBytesSent')

    def bytes_received(self) -> int:
        return self.__LAN_STATS.get('NewBytesReceived')

    def packets_sent(self) -> int:
        return self.__LAN_STATS.get('NewPacketsSent')

    def packets_received(self) -> int:
        return self.__LAN_STATS.get('NewPacketsReceived')
