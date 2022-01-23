from dataclasses import dataclass

from models.fritzbox_model_interface import FritzboxModelInterface
from modules.influx_print import InfluxPrint


@dataclass
class FritzboxPhoneModel(FritzboxModelInterface):
    """Contains Phone data"""

    def __init__(self, count_missed_calls: int, count_out_calls: int, count_received_calls: int,
                 time_missed_calls: int, time_out_calls: int, time_received_calls: int):
        self.count_missed_calls: int = count_missed_calls
        self.count_out_calls: int = count_out_calls
        self.count_received_calls: int = count_received_calls
        self.time_missed_calls: int = time_missed_calls
        self.time_out_calls: int = time_out_calls
        self.time_received_calls: int = time_received_calls

    def influx_data(self) -> str:
        influx_result = list()
        InfluxPrint.append(influx_result, "CountMissedCalls", self.count_missed_calls)
        InfluxPrint.append(influx_result, "CountOutCalls", self.count_out_calls)
        InfluxPrint.append(influx_result, "CountReceivedCalls", self.count_received_calls)
        InfluxPrint.append(influx_result, "TimeReceivedCalls", self.time_received_calls)
        InfluxPrint.append(influx_result, "TimeOutCalls", self.time_out_calls)
        InfluxPrint.append(influx_result, "TimeReceivedCalls", self.time_received_calls)
        return ",".join(influx_result)
