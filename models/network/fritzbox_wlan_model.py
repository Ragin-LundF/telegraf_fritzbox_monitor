from dataclasses import dataclass

from models.fritzbox_model_interface import FritzboxModelInterface
from modules.influx_print import InfluxPrint


@dataclass
class FritzboxWLANModel(FritzboxModelInterface):
    """Contains WLAN data"""
    def __init__(self, ssid: str, channel: int, clients: int, packets_sent: int,
                 packets_received: int):
        self.ssid: str = ssid
        self.channel: int = channel
        self.clients: int = clients
        self.packets_sent: int = packets_sent
        self.packets_received: int = packets_received

    def influx_data(self) -> str:
        influx_result = list()
        influx_result.append(InfluxPrint.tag_str("SSID", self.ssid))
        influx_result.append(InfluxPrint.tag_int("Channel", self.channel))
        influx_result.append(InfluxPrint.tag_int("ClientsNumber", self.clients))
        influx_result.append(InfluxPrint.tag_int("PacketsSent", self.packets_sent))
        influx_result.append(InfluxPrint.tag_int("PacketsReceived", self.packets_received))

        return ",".join(influx_result)
