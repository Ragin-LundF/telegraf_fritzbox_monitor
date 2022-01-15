from models.network.fritzbox_wan import FritzboxWAN
from modules.fritz_connect import FritzboxConnect


class FritzboxConnectWAN:
    def __init__(self, fc: FritzboxConnect):
        self.FC = fc

    def _wan_stats(self):
        return self.FC.FSTAT

    def stats(self) -> FritzboxWAN:
        wan_model = FritzboxWAN(
            is_connected=self.is_connected(),
            is_linked=self.is_linked(),
            connection_uptime=self.connection_uptime(),
            bytes_sent=self.bytes_sent(),
            bytes_received=self.bytes_received(),
            external_ipv4=self.external_ipv4(),
            external_ipv6=self.external_ipv6(),
            external_ipv6_info=self.external_ipv6_info(),
            max_linked_bitrate_downstream=self.max_linked_bitrate_downstream(),
            max_linked_bitrate_upstream=self.max_linked_bitrate_upstream(),
            max_linked_bitrate_downstream_str=self.max_linked_bitrate_downstream_str(),
            max_linked_bitrate_upstream_str=self.max_linked_bitrate_upstream_str(),
            max_bitrate_downstream=self.max_bitrate_downstream(),
            max_bitrate_upstream=self.max_bitrate_upstream(),
            max_bitrate_downstream_str=self.max_bitrate_downstream_str(),
            max_bitrate_upstream_str=self.max_bitrate_upstream_str(),
            max_byterate_downstream=self.max_byterate_downstream(),
            max_byterate_upstream=self.max_byterate_upstream(),
            transmission_rate_downstream=self.transmission_rate_downstream(),
            transmission_rate_upstream=self.transmission_rate_upstream(),
            transmission_rate_downstream_str=self.transmission_rate_downstream_str(),
            transmission_rate_upstream_str=self.transmission_rate_upstream_str(),
        )

        return wan_model

    def is_connected(self) -> bool:
        return self._wan_stats().is_connected

    def is_linked(self) -> bool:
        return self._wan_stats().is_linked

    def connection_uptime(self) -> int:
        return self._wan_stats().connection_uptime

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

    def max_linked_bitrate_upstream(self) -> int:
        return self._wan_stats().max_linked_bit_rate[0]

    def max_linked_bitrate_downstream(self) -> int:
        return self._wan_stats().max_linked_bit_rate[1]

    def max_linked_bitrate_upstream_str(self) -> str:
        return self._wan_stats().str_max_linked_bit_rate[0]

    def max_linked_bitrate_downstream_str(self) -> str:
        return self._wan_stats().str_max_linked_bit_rate[1]

    def max_bitrate_upstream(self) -> int:
        return self._wan_stats().max_bit_rate[0]

    def max_bitrate_downstream(self) -> int:
        return self._wan_stats().max_bit_rate[1]

    def max_bitrate_upstream_str(self) -> str:
        return self._wan_stats().str_max_bit_rate[0]

    def max_bitrate_downstream_str(self) -> str:
        return self._wan_stats().str_max_bit_rate[1]

    def max_byterate_upstream(self) -> int:
        return self._wan_stats().max_byte_rate[0]

    def max_byterate_downstream(self) -> int:
        return self._wan_stats().max_byte_rate[1]

    def transmission_rate_upstream(self) -> int:
        return self._wan_stats().transmission_rate[0]

    def transmission_rate_downstream(self) -> int:
        return self._wan_stats().transmission_rate[1]

    def transmission_rate_upstream_str(self) -> str:
        return self._wan_stats().str_transmission_rate[0]

    def transmission_rate_downstream_str(self) -> str:
        return self._wan_stats().str_transmission_rate[1]
