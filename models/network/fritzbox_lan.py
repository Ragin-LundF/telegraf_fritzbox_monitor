from dataclasses import dataclass

from models.fritzbox_model_interface import FritzboxModelInterface
from modules.influx_print import InfluxPrint


@dataclass
class FritzboxLAN(FritzboxModelInterface):
    """Contains LAN data"""

    def __init__(self, bytes_sent: int, bytes_received: int, packets_sent: int, packets_received: int):
        self.bytes_sent: int = bytes_sent
        self.bytes_received: int = bytes_received
        self.packets_sent: int = packets_sent
        self.packets_received: int = packets_received

    def influx_data(self) -> str:
        influx_result = list()
        influx_result.append(InfluxPrint.tag_int("BytesSent", self.bytes_sent))
        influx_result.append(InfluxPrint.tag_int("BytesReceived", self.bytes_received))
        influx_result.append(InfluxPrint.tag_int("PacketsSent", self.packets_sent))
        influx_result.append(InfluxPrint.tag_int("PacketsReceived", self.packets_received))

        return ",".join(influx_result)
