from dataclasses import dataclass


@dataclass
class FritzboxLAN:
    """Contains LAN data"""
    bytes_sent: int
    bytes_received: int
    packets_sent: int
    packets_received: int

    def __init__(self, bytes_sent: int, bytes_received: int, packets_sent: int, packets_received: int):
        self.bytes_sent = bytes_sent
        self.bytes_received = bytes_received
        self.packets_sent = packets_sent
        self.packets_received = packets_received

    def influx_data(self) -> str:
        influx_result = list()
        influx_result.append(f"BytesSent={self.bytes_sent}i")
        influx_result.append(f"BytesReceived={self.bytes_received}i")
        influx_result.append(f"PacketsSent={self.packets_sent}i")
        influx_result.append(f"PacketsReceived={self.packets_received}i")

        return ",".join(influx_result)
