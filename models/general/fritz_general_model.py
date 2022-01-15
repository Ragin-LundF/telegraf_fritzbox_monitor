from dataclasses import dataclass

from models.fritzbox_model_interface import FritzboxModelInterface
from modules.influx_print import InfluxPrint


@dataclass
class FritzboxGeneralModel(FritzboxModelInterface):
    """Contains general data"""
    def __init__(self, model: str, firmware: str, wan_access_type: str, serial_number: str):
        self.model: str = model
        self.firmware: str = firmware
        self.wan_access_type: str = wan_access_type
        self.serial_number: str = serial_number

    def influx_data(self) -> str:
        influx_result = list()
        influx_result.append(InfluxPrint.tag_str("ModelName", self.model))
        influx_result.append(InfluxPrint.tag_str("Firmware", self.firmware))
        influx_result.append(InfluxPrint.tag_str("WANAccessType", self.wan_access_type))
        influx_result.append(InfluxPrint.tag_str("SerialNumber", self.serial_number))

        return ",".join(influx_result)

