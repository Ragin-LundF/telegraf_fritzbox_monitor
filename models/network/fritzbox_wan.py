from dataclasses import dataclass

from modules.influx_print import InfluxPrint


@dataclass
class FritzboxWAN:
    """Contains WAN data"""

    def __init__(self, is_connected: bool, is_linked: bool, connection_uptime: int, bytes_sent: int,
                 bytes_received: int, external_ipv4: str, external_ipv6: str, external_ipv6_info: dict,
                 max_linked_bitrate_downstream: int, max_linked_bitrate_upstream: int,
                 max_linked_bitrate_downstream_str: str, max_linked_bitrate_upstream_str: str,
                 max_bitrate_downstream: int, max_bitrate_upstream: int, max_bitrate_downstream_str: str,
                 max_bitrate_upstream_str: str, max_byterate_downstream: float, max_byterate_upstream: float,
                 transmission_rate_downstream: int, transmission_rate_upstream: int,
                 transmission_rate_downstream_str: str, transmission_rate_upstream_str: str):
        self.is_connected: bool = is_connected
        self.is_linked: bool = is_linked
        self.connection_uptime: int = connection_uptime
        self.bytes_sent: int = bytes_sent
        self.bytes_received: int = bytes_received
        self.external_ipv4: str = external_ipv4
        self.external_ipv6: str = external_ipv6
        self.external_ipv6_info: dict = external_ipv6_info
        self.max_linked_bitrate_downstream: int = max_linked_bitrate_downstream
        self.max_linked_bitrate_upstream: int = max_linked_bitrate_upstream
        self.max_linked_bitrate_downstream_str: str = max_linked_bitrate_downstream_str
        self.max_linked_bitrate_upstream_str: str = max_linked_bitrate_upstream_str
        self.max_bitrate_downstream: int = max_bitrate_downstream
        self.max_bitrate_upstream: int = max_bitrate_upstream
        self.max_bitrate_downstream_str: str = max_bitrate_downstream_str
        self.max_bitrate_upstream_str: str = max_bitrate_upstream_str
        self.max_byterate_downstream: float = max_byterate_downstream
        self.max_byterate_upstream: float = max_byterate_upstream
        self.transmission_rate_downstream: int = transmission_rate_downstream
        self.transmission_rate_upstream: int = transmission_rate_upstream
        self.transmission_rate_downstream_str: str = transmission_rate_downstream_str
        self.transmission_rate_upstream_str: str = transmission_rate_upstream_str

    def influx_data(self) -> str:
        influx_result = list()
        influx_result = InfluxPrint.append(influx_result, "Connected", self.is_connected)
        influx_result = InfluxPrint.append(influx_result, "Linked", self.is_linked)
        influx_result = InfluxPrint.append(influx_result, "ConnectionTime", self.connection_uptime)
        influx_result = InfluxPrint.append(influx_result, "TotalBytesSent64", self.bytes_sent)
        influx_result = InfluxPrint.append(influx_result, "TotalBytesReceived64", self.bytes_received)
        influx_result = InfluxPrint.append(influx_result, "ExternalIPAddress", self.external_ipv4)
        influx_result = InfluxPrint.append(influx_result, "ExternalIPv6Address", self.external_ipv6)
        influx_result = InfluxPrint.append(influx_result, "Layer1DownstreamMaxBitRate", self.max_linked_bitrate_downstream)
        influx_result = InfluxPrint.append(influx_result, "Layer1UpstreamMaxBitRate", self.max_linked_bitrate_upstream)
        # influx_result = InfluxPrint.append(influx_result, "max_bitrate_downstream", self.max_bitrate_downstream)
        # influx_result = InfluxPrint.append(influx_result, "max_bitrate_upstream", self.max_bitrate_upstream)
        # influx_result = InfluxPrint.append(influx_result, "max_byterate_downstream", self.max_byterate_downstream)
        # influx_result = InfluxPrint.append(influx_result, "max_byterate_upstream", self.max_byterate_upstream)
        influx_result = InfluxPrint.append(influx_result, "TransmissionRateDownstream", self.transmission_rate_downstream)
        influx_result = InfluxPrint.append(influx_result, "TransmissionRateUpstream", self.transmission_rate_upstream)

        return ",".join(influx_result)
