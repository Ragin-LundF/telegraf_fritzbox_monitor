from models.network.fritzbox_wan import FritzboxWAN
from modules.fritz_connect import FritzboxConnect


class FritzboxConnectWAN:
    def __init__(self, fc: FritzboxConnect):
        self.FC = fc

    def _wan_stats(self):
        return self.FC.FSTAT

    def stats(self) -> FritzboxWAN:
        wan_model = FritzboxWAN(
            bytes_sent=self.bytes_sent(),
            bytes_received=self.bytes_received(),
            external_ipv4=self.external_ipv4(),
            external_ipv6=self.external_ipv6(),
            external_ipv6_info=self.external_ipv6_info()
        )

        return wan_model

    def bytes_sent(self) -> int:
        return self._wan_stats().bytes_sent

    def bytes_received(self) -> int:
        return self._wan_stats().bytes_received

    def external_ipv4(self) -> str:
        return self._wan_stats().external_ip

    def external_ipv6(self) -> str:
        return self._wan_stats().external_ipv6

    def external_ipv6_info(self) -> dict:
        return self._wan_stats().external_ipv6_info
