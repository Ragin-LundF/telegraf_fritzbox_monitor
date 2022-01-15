from models.network.fritzbox_dsl_model import FritzboxDSLModel
from modules.fritz_connect import FritzboxConnect


class FritzboxConnectDSL:
    def __init__(self, fc: FritzboxConnect):
        self.__DSL_INFO = fc.read_module('WANDSLInterfaceConfig1', 'GetInfo')
        self.__DSL_STATS_TOTAL = fc.read_module('WANDSLInterfaceConfig1', 'GetStatisticsTotal')

    def stats(self) -> FritzboxDSLModel:
        lan_model = FritzboxDSLModel(
            downstream_curr_rate=self.downstream_curr_rate(),
            upstream_curr_rate=self.upstream_curr_rate(),
            downstream_max_rate=self.downstream_max_rate(),
            upstream_max_rate=self.upstream_max_rate(),
            downstream_noise_margin=self.downstream_noise_margin(),
            upstream_noise_margin=self.upstream_noise_margin(),
            downstream_power=self.downstream_power(),
            upstream_power=self.upstream_power(),
            downstream_attenuation=self.downstream_attenuation(),
            upstream_attenuation=self.upstream_attenuation(),
            errors_fec=self.errors_fec(),
            errors_fec_local=self.errors_fec_local(),
            errors_crc=self.errors_crc(),
            errors_crc_local=self.errors_crc_local(),
            errors_hec=self.errors_hec(),
            errors_hec_local=self.errors_hec_local()
        )

        return lan_model

    def downstream_curr_rate(self) -> int:
        return self.__DSL_INFO.get('NewDownstreamCurrRate')

    def upstream_curr_rate(self) -> int:
        return self.__DSL_INFO.get('NewUpstreamCurrRate')

    def downstream_max_rate(self) -> int:
        return self.__DSL_INFO.get('NewDownstreamMaxRate')

    def upstream_max_rate(self) -> int:
        return self.__DSL_INFO.get('NewUpstreamMaxRate')

    def downstream_noise_margin(self) -> int:
        return self.__DSL_INFO.get('NewDownstreamNoiseMargin')

    def upstream_noise_margin(self) -> int:
        return self.__DSL_INFO.get('NewUpstreamNoiseMargin')

    def downstream_power(self) -> int:
        return self.__DSL_INFO.get('NewDownstreamPower')

    def upstream_power(self) -> int:
        return self.__DSL_INFO.get('NewUpstreamPower')

    def downstream_attenuation(self) -> int:
        return self.__DSL_INFO.get('NewDownstreamAttenuation')

    def upstream_attenuation(self) -> int:
        return self.__DSL_INFO.get('NewUpstreamAttenuation')

    def errors_fec(self) -> int:
        return self.__DSL_STATS_TOTAL.get('NewFECErrors')

    def errors_fec_local(self) -> int:
        return self.__DSL_STATS_TOTAL.get('NewATUCFECErrors')

    def errors_crc(self) -> int:
        return self.__DSL_STATS_TOTAL.get('NewCRCErrors')

    def errors_crc_local(self) -> int:
        return self.__DSL_STATS_TOTAL.get('NewATUCCRCErrors')

    def errors_hec(self) -> int:
        return self.__DSL_STATS_TOTAL.get('NewHECErrors')

    def errors_hec_local(self) -> int:
        return self.__DSL_STATS_TOTAL.get('NewATUCHECErrors')

