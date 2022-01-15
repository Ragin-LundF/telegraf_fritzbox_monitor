from dataclasses import dataclass

from models.fritzbox_model_interface import FritzboxModelInterface
from modules.influx_print import InfluxPrint


@dataclass
class FritzboxDSLModel(FritzboxModelInterface):
    """Contains DSL data"""

    def __init__(self, downstream_curr_rate: int, upstream_curr_rate: int, downstream_max_rate: int,
                 upstream_max_rate: int, downstream_noise_margin: int, upstream_noise_margin: int,
                 downstream_power: int, upstream_power: int, downstream_attenuation: int, upstream_attenuation: int,
                 errors_fec: int, errors_fec_local: int, errors_crc: int, errors_crc_local: int,
                 errors_hec: int, errors_hec_local: int):
        self.downstream_curr_rate: int = downstream_curr_rate
        self.upstream_curr_rate: int = upstream_curr_rate
        self.downstream_max_rate: int = downstream_max_rate
        self.upstream_max_rate: int = upstream_max_rate
        self.downstream_noise_margin: int = downstream_noise_margin
        self.upstream_noise_margin: int = upstream_noise_margin
        self.downstream_power: int = downstream_power
        self.upstream_power: int = upstream_power
        self.downstream_attenuation: int = downstream_attenuation
        self.upstream_attenuation: int = upstream_attenuation
        self.errors_fec: int = errors_fec
        self.errors_fec_local: int = errors_fec_local
        self.errors_crc: int = errors_crc
        self.errors_crc_local: int = errors_crc_local
        self.errors_hec: int = errors_hec
        self.errors_hec_local: int = errors_hec_local

    def influx_data(self) -> str:
        influx_result = list()
        InfluxPrint.append(influx_result, "DownstreamCurrRate", self.downstream_curr_rate)
        InfluxPrint.append(influx_result, "UpstreamCurrRate", self.upstream_curr_rate)
        InfluxPrint.append(influx_result, "DownstreamMaxRate", self.downstream_max_rate)
        InfluxPrint.append(influx_result, "DownstreamMaxRate", self.upstream_max_rate)
        InfluxPrint.append(influx_result, "DownstreamNoiseMargin", self.downstream_noise_margin)
        InfluxPrint.append(influx_result, "UpstreamNoiseMargin", self.upstream_noise_margin)
        InfluxPrint.append(influx_result, "DownstreamPower", self.downstream_power)
        InfluxPrint.append(influx_result, "UpstreamPower", self.upstream_power)
        InfluxPrint.append(influx_result, "DownstreamAttenuation", self.downstream_attenuation)
        InfluxPrint.append(influx_result, "UpstreamAttenuation", self.upstream_attenuation)
        InfluxPrint.append(influx_result, "FECErrors", self.errors_fec)
        InfluxPrint.append(influx_result, "ATUCFECErrors", self.errors_fec_local)
        InfluxPrint.append(influx_result, "CRCErrors", self.errors_crc)
        InfluxPrint.append(influx_result, "ATUCCRCErrors", self.errors_crc_local)
        InfluxPrint.append(influx_result, "HECErrors", self.errors_hec)
        InfluxPrint.append(influx_result, "ATUCHECErrors", self.errors_hec_local)

        return ",".join(influx_result)
