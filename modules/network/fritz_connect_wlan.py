from enum import Enum

from models.network.fritzbox_wlan import FritzboxWLAN
from modules.fritz_connect import FritzboxConnect


class WLANType(Enum):
    WLAN_2_4_GHZ = "WLANConfiguration1"
    WLAN_5_GHZ = "WLANConfiguration2"
    WLAN_GUEST = "WLANConfiguration3"


class FritzboxConnectWLAN:
    def __init__(self, fc: FritzboxConnect, wlan_type: WLANType):
        self.__WLAN_INFO = fc.read_module(wlan_type.value, 'GetInfo')
        self.__WLAN_STATS = fc.read_module(wlan_type.value, 'GetStatistics')
        self.__WLAN_TOTAL_ASSOC = fc.read_module(wlan_type.value, 'GetTotalAssociations')

    def stats(self) -> FritzboxWLAN:
        wlan_model = FritzboxWLAN(
            ssid=self.ssid(),
            channel=self.channel(),
            clients=self.clients(),
            packets_sent=self.packets_sent(),
            packets_received=self.packets_received()
        )

        return wlan_model

    def ssid(self) -> str:
        return self.__WLAN_INFO.get('NewSSID')

    def channel(self) -> int:
        return self.__WLAN_INFO.get('NewChannel')

    def clients(self) -> int:
        return self.__WLAN_TOTAL_ASSOC.get('NewTotalAssociations')

    def packets_sent(self) -> int:
        return self.__WLAN_STATS.get('NewTotalPacketsSent')

    def packets_received(self) -> int:
        return self.__WLAN_STATS.get('NewTotalPacketsReceived')
