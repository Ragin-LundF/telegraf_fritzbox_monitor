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
        InfluxPrint.append(influx_result, "SSID", self.ssid)
        InfluxPrint.append(influx_result, "Channel", self.channel)
        InfluxPrint.append(influx_result, "ClientsNumber", self.clients)
        InfluxPrint.append(influx_result, "PacketsSent", self.packets_sent)
        InfluxPrint.append(influx_result, "PacketsReceived", self.packets_received)

        return ",".join(influx_result)
