from models.general.fritz_general_model import FritzboxGeneralModel
from modules.fritz_connect import FritzboxConnect


class FritzboxConnectGeneral:
    def __init__(self, fc: FritzboxConnect):
        self.__FC_STATUS = fc.status()
        self.__DEVICE_INFO = fc.read_module('DeviceInfo1', 'GetInfo')

    def stats(self) -> FritzboxGeneralModel:
        general_model = FritzboxGeneralModel(
            model=self.model(),
            firmware=self.firmware(),
            wan_access_type=self.wan_access_type(),
            serial_number=self.serial_number()
        )

        return general_model

    def model(self) -> str:
        return self.__FC_STATUS.modelname

    def firmware(self) -> str:
        return self.__FC_STATUS.fc.system_version

    def wan_access_type(self) -> str:
        return self.__DEVICE_INFO.get('WANAccessType')

    def serial_number(self) -> str:
        return self.__DEVICE_INFO.get('NewSerialNumber')
