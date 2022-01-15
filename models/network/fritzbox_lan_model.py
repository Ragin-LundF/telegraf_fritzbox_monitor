from dataclasses import dataclass

from models.fritzbox_model_interface import FritzboxModelInterface
from modules.influx_print import InfluxPrint


@dataclass
class FritzboxLANModel(FritzboxModelInterface):
    """Contains LAN data"""

    def __init__(self, bytes_sent: int, bytes_received: int, packets_sent: int, packets_received: int):
        self.bytes_sent: int = bytes_sent
        self.bytes_received: int = bytes_received
        self.packets_sent: int = packets_sent
        self.packets_received: int = packets_received

    def influx_data(self) -> str:
        influx_result = list()
        InfluxPrint.append(influx_result, "BytesSent", self.bytes_sent)
        InfluxPrint.append(influx_result, "BytesReceived", self.bytes_received)
        InfluxPrint.append(influx_result, "PacketsSent", self.packets_sent)
        InfluxPrint.append(influx_result, "PacketsReceived", self.packets_received)

        return ",".join(influx_result)
