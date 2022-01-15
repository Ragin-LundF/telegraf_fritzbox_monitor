class InfluxPrint:
    def __init__(self, fritzbox_id: str, fritzbox_name: str):
        self.__FB_ID = fritzbox_id
        self.__FB_NAME = fritzbox_name

    def print(self, tag: str, data: str):
        influx = self.__FB_ID + ',' + self.__FB_NAME + ',source=' + tag + ' ' + data
        print(influx)
