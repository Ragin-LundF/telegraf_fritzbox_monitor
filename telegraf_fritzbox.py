import argparse
import sys

from fritzconnection.cli.utils import get_cli_arguments

from modules.configuration import Configuration
from modules.fritz_connect import FritzboxConnect
from modules.general.fritzbox_general import FritzboxConnectGeneral
from modules.general.fritzbox_status import FritzboxConnectStatus
from modules.influx_print import InfluxPrint
from modules.network.fritz_connect_dsl import FritzboxConnectDSL
from modules.network.fritz_connect_lan import FritzboxConnectLAN
from modules.network.fritz_connect_network import FritzboxConnectNetwork
from modules.network.fritz_connect_wan import FritzboxConnectWAN
from modules.network.fritz_connect_wlan import FritzboxConnectWLAN, WLANType

# Default database for InfluxDB
from modules.phone.fritz_connect_phone import FritzboxConnectPhone


class Application:
    def __init__(self):
        self.__config: Configuration = Configuration()

    def execute(self) -> None:
        args = self.__get_cli_args()
        if not args.password and self.__config.get().connection_password is None:
            print('Please configure a password to access the Fritz!Box.')
            self.__show_help()
            sys.exit(1)

        if args.address:
            self.__config.get().set_connection_address(args.address)
        if args.username:
            self.__config.get().set_connection_username(args.username)
        if args.password:
            self.__config.get().set_connection_password(args.password)

        try:
            fritz_connect = FritzboxConnect(config=self.__config.get())
        except BaseException as exception:
            print(exception)
            print("Cannot connect to Fritz!Box. ")
            self.__show_help()
            sys.exit(1)

        influxp = InfluxPrint(args.database, self.__fritzbox_host_name(fritz_connect))
        influxp.print("general", FritzboxConnectGeneral(fritz_connect).stats().influx_data())
        influxp.print("status", FritzboxConnectStatus(fritz_connect).stats().influx_data())
        influxp.print("lan", FritzboxConnectLAN(fritz_connect).stats().influx_data())
        influxp.print("dsl", FritzboxConnectDSL(fritz_connect).stats().influx_data())
        influxp.print("wlan_2.4GHz", FritzboxConnectWLAN(fritz_connect, WLANType.WLAN_2_4_GHZ).stats().influx_data())
        influxp.print("wlan_5GHz", FritzboxConnectWLAN(fritz_connect, WLANType.WLAN_5_GHZ).stats().influx_data())
        influxp.print("wlan_Guest", FritzboxConnectWLAN(fritz_connect, WLANType.WLAN_GUEST).stats().influx_data())
        influxp.print("wan", FritzboxConnectWAN(fritz_connect).stats().influx_data())
        influxp.print("network", FritzboxConnectNetwork(fritz_connect).stats().influx_data())
        if self.__config.get().features_enable_phone_call_tracking:
            influxp.print("phone", FritzboxConnectPhone(fritz_connect).stats().influx_data())

    def __fritzbox_host_name(self, fc: FritzboxConnect) -> str:
        host_config = fc.read_module('LANHostConfigManagement1', 'GetInfo')
        try:
            return host_config['NewDomainName']
        except KeyError:
            return "fritz.box"

    def __show_help(self) -> None:
        print()
        print('Options:')
        print('-i | --ip-address [FRITZ_IP_ADDRESS]: '
              'IP-address of the Fritz!Box (Default 169.254.1.1)')
        print('--port [FRITZ_TCP_PORT]             : '
              'Port of the Fritz!Box (Default: 49000)')
        print('-u | --username [FRITZ_USERNAME]    : '
              'Fritz!Box username (Default: admin)')
        print('-p | --password [FRITZ_PASSWORD]    : '
              'Fritz!Box password for the monitoring user.')
        print('-e | --encrypt [ENCRYPT]            : '
              'Use a secure connection to your Fritz!Box. Can be True or False (Default: False)')
        print(f'-d | --database [FRITZBOX_DATABASE]: '
              f'Fritz!Box Database. (Default: {self.__config.get().defaults_database})')

    def __get_cli_args(self) -> argparse.Namespace:
        args = get_cli_arguments()
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--database',
                            nargs='?', default=self.__config.get().defaults_database, const=None,
                            dest='database',
                            help='Specify a database name of the InfluxDB.'
                                 'Default: %s' % self.__config.get().defaults_database)
        return parser.parse_known_args(namespace=args)[0]


if __name__ == '__main__':
    Application().execute()
