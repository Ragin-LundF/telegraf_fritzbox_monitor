from dataclasses import dataclass

from models.fritzbox_model_interface import FritzboxModelInterface
from modules.influx_print import InfluxPrint


@dataclass
class FritzboxStatusModel(FritzboxModelInterface):
    """Contains status data"""
    def __init__(self, uptime: int, connection_status: str, last_error: str):
        self.uptime: int = uptime
        self.connection_status: str = connection_status
        self.last_error: str = last_error

    def influx_data(self) -> str:
        influx_result = list()
        influx_result.append(InfluxPrint.tag_int("UpTime", self.uptime))
        influx_result.append(InfluxPrint.tag_str("ConnectionStatus", self.connection_status))
        influx_result.append(InfluxPrint.tag_str("LastError", self.last_error))

        return ",".join(influx_result)

