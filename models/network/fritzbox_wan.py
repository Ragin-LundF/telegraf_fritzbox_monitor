from dataclasses import dataclass

from modules.influx_print import InfluxPrint


@dataclass
class FritzboxWAN:
    """Contains WAN data"""
    def __init__(self, bytes_sent: int, bytes_received: int, external_ipv4: str, external_ipv6: str,
                 external_ipv6_info: dict):
        self.bytes_sent: int = bytes_sent
        self.bytes_received: int = bytes_received
        self.external_ipv4: str = external_ipv4
        self.external_ipv6: str = external_ipv6
        self.external_ipv6_info: dict = external_ipv6_info

    def influx_data(self) -> str:
        influx_result = list()
        influx_result.append(InfluxPrint.tag_int("BytesSent", self.bytes_sent))
        influx_result.append(InfluxPrint.tag_int("BytesReceived", self.bytes_received))
        influx_result.append(InfluxPrint.tag_str("ExternalIPAddress", self.external_ipv4))
        influx_result.append(InfluxPrint.tag_str("ExternalIPv6Address", self.external_ipv6))

        return ",".join(influx_result)
