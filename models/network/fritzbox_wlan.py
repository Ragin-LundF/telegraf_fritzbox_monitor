from dataclasses import dataclass


@dataclass
class FritzboxWLAN:
    """Contains WLAN data"""
    ssid: str
    channel: int
    clients: int
    bytes_sent: int
    bytes_received: int
    packets_sent: int
    packets_received: int

    def __init__(self, ssid: str, channel: int, clients: int, bytes_sent: int, bytes_received: int, packets_sent: int,
                 packets_received: int):
        self.ssid = ssid
        self.channel = channel
        self.clients = clients
        self.bytes_sent = bytes_sent
        self.bytes_received = bytes_received
        self.packets_sent = packets_sent
        self.packets_received = packets_received

    def influx_data(self) -> str:
        influx_result = list()
        influx_result.append(f'SSID="{self.ssid}"')
        influx_result.append(f"Channel={self.channel}i")
        influx_result.append(f"ClientsNumber={self.clients}i")
        influx_result.append(f"BytesSent={self.bytes_sent}i")
        influx_result.append(f"BytesReceived={self.bytes_received}i")
        influx_result.append(f"PacketsSent={self.packets_sent}i")
        influx_result.append(f"PacketsReceived={self.packets_received}i")

        return ",".join(influx_result)
