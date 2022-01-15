class InfluxPrint:
    def __init__(self, fritzbox_id: str, fritzbox_name: str):
        self.__FB_ID = fritzbox_id
        self.__FB_NAME = fritzbox_name

    def print(self, tag: str, data: str):
        if data:
            influx = self.__FB_ID + ',' + self.__FB_NAME + ',source=' + tag + ' ' + data
            print(influx)

    @staticmethod
    def append(influx_list: list, tag_name: str, value):
        if isinstance(value, bool):
            influx_list.append(InfluxPrint.tag_bool(tag_name, value))
        elif isinstance(value, int):
            influx_list.append(InfluxPrint.tag_int(tag_name, value))
        elif isinstance(value, float):
            influx_list.append(InfluxPrint.tag_float(tag_name, value))
        elif isinstance(value, str):
            if value:
                influx_list.append(InfluxPrint.tag_str(tag_name, value))
        elif value is None:
            return influx_list
        else:
            raise Exception("Unable to map value for influxdb")
        return influx_list

    @staticmethod
    def tag_int(tag_name: str, value: int) -> str:
        return f'{tag_name}={value}i'

    @staticmethod
    def tag_float(tag_name: str, value: float) -> str:
        return f'{tag_name}={value}'

    @staticmethod
    def tag_bool(tag_name: str, value: bool) -> str:
        return f'{tag_name}={value}'

    @staticmethod
    def tag_str(tag_name: str, value: str) -> str:
        return f'{tag_name}="{value}"'
