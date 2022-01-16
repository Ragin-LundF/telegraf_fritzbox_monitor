from dataclasses import dataclass

from models.fritzbox_model_interface import FritzboxModelInterface
from modules.influx_print import InfluxPrint


@dataclass
class FritzboxWANModel(FritzboxModelInterface):
    """Contains WAN data"""

    def __init__(self, is_connected: bool, is_linked: bool, connection_uptime: int, bytes_sent: float,
                 bytes_received: float, external_ipv4: str, external_ipv6: str, external_ipv6_info: dict,
                 max_linked_bitrate_downstream: int, max_linked_bitrate_upstream: int,
                 max_linked_bitrate_downstream_str: str, max_linked_bitrate_upstream_str: str,
                 max_bitrate_downstream: int, max_bitrate_upstream: int, max_bitrate_downstream_str: str,
                 max_bitrate_upstream_str: str, max_byterate_downstream: float, max_byterate_upstream: float,
                 transmission_rate_downstream: int, transmission_rate_upstream: int,
                 transmission_rate_downstream_str: str, transmission_rate_upstream_str: str,
                 current_downstream_rate: int, current_upstream_rate: int):
        self.is_connected: bool = is_connected
        self.is_linked: bool = is_linked
        self.connection_uptime: int = connection_uptime
        self.bytes_sent: float = bytes_sent
        self.bytes_received: float = bytes_received
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
        self.current_downstream_rate: int = current_downstream_rate
        self.current_upstream_rate: int = current_upstream_rate

    def influx_data(self) -> str:
        influx_result = list()
        InfluxPrint.append(influx_result, "Connected", self.is_connected)
        InfluxPrint.append(influx_result, "Linked", self.is_linked)
        InfluxPrint.append(influx_result, "ConnectionTime", self.connection_uptime)
        InfluxPrint.append_float(influx_result, "TotalBytesSent64", self.bytes_sent)
        InfluxPrint.append_float(influx_result, "TotalBytesReceived64", self.bytes_received)
        InfluxPrint.append(influx_result, "ExternalIPAddress", self.external_ipv4)
        InfluxPrint.append(influx_result, "ExternalIPv6Address", self.external_ipv6)
        InfluxPrint.append(influx_result, "Layer1DownstreamMaxBitRate", self.max_linked_bitrate_downstream)
        InfluxPrint.append(influx_result, "Layer1UpstreamMaxBitRate", self.max_linked_bitrate_upstream)
        # InfluxPrint.append(influx_result, "max_bitrate_downstream", self.max_bitrate_downstream)
        # InfluxPrint.append(influx_result, "max_bitrate_upstream", self.max_bitrate_upstream)
        InfluxPrint.append(influx_result, "max_byterate_downstream", self.max_byterate_downstream)
        InfluxPrint.append(influx_result, "max_byterate_upstream", self.max_byterate_upstream)
        InfluxPrint.append(influx_result, "TransmissionRateDownstream", self.transmission_rate_downstream)
        InfluxPrint.append(influx_result, "TransmissionRateUpstream", self.transmission_rate_upstream)
        InfluxPrint.append(influx_result, "ByteReceiveRate", self.current_downstream_rate)
        InfluxPrint.append(influx_result, "ByteSendRate", self.current_upstream_rate)

        return ",".join(influx_result)
