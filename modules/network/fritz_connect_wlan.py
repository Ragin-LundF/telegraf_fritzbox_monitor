from enum import Enum

from models.network.fritzbox_wlan import FritzboxWLAN
from modules.fritz_connect import FritzboxConnect


class WLANType(Enum):
    WLAN_2_4_GHZ = "WLANConfiguration1"
    WLAN_5_GHZ = "WLANConfiguration2"
    WLAN_GUEST = "WLANConfiguration3"


class FritzboxConnectWLAN:
    def __init__(self, fc: FritzboxConnect, wlan_type: WLANType):
        self.FC = fc
        self.WLAN_TYPE = wlan_type

    def _wlan_info(self):
        return self.FC.read_module(self.WLAN_TYPE.value, 'GetInfo')

    def _wlan_stats(self):
        return self.FC.read_module(self.WLAN_TYPE.value, 'GetStatistics')

    def _wlan_total_assoc(self):
        return self.FC.read_module(self.WLAN_TYPE.value, 'GetTotalAssociations')

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
        return self._wlan_info().get('NewSSID')

    def channel(self) -> int:
        return self._wlan_info().get('NewChannel')

    def clients(self) -> int:
        return self._wlan_total_assoc().get('NewTotalAssociations')

    def packets_sent(self) -> int:
        return self._wlan_stats().get('NewTotalPacketsSent')

    def packets_received(self) -> int:
        return self._wlan_stats().get('NewTotalPacketsReceived')
