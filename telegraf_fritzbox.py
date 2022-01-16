import argparse
import sys

from fritzconnection.cli.utils import get_cli_arguments

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
FRITZBOX_DEFAULT_DATABASE = 'FritzBox'


def fritzbox_host_name(fc: FritzboxConnect) -> str:
    host_config = fc.read_module('LANHostConfigManagement1', 'GetInfo')
    try:
        return host_config['NewDomainName']
    except KeyError:
        return "fritz.box"


def show_help() -> None:
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
          f'Fritz!Box Database. (Default: {FRITZBOX_DEFAULT_DATABASE})')


def get_cli_args() -> argparse.Namespace:
    args = get_cli_arguments()
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--database',
                        nargs='?', default=FRITZBOX_DEFAULT_DATABASE, const=None,
                        dest='database',
                        help='Specify a database name of the InfluxDB.'
                             'Default: %s' % FRITZBOX_DEFAULT_DATABASE)
    return parser.parse_known_args(namespace=args)[0]


def execute() -> None:
    args = get_cli_args()
    if not args.password:
        print('Please configure a password to access the Fritz!Box.')
        show_help()
        sys.exit(1)
    else:
        try:
            fritz_connect = FritzboxConnect(
                address=args.address,
                username=args.username,
                password=args.password,
                port=args.port)
        except BaseException as exception:
            print(exception)
            print("Cannot connect to Fritz!Box. ")
            show_help()
            sys.exit(1)

    influxp = InfluxPrint(args.database, fritzbox_host_name(fritz_connect))
    influxp.print("general", FritzboxConnectGeneral(fritz_connect).stats().influx_data())
    influxp.print("status", FritzboxConnectStatus(fritz_connect).stats().influx_data())
    influxp.print("lan", FritzboxConnectLAN(fritz_connect).stats().influx_data())
    influxp.print("dsl", FritzboxConnectDSL(fritz_connect).stats().influx_data())
    influxp.print("wlan_2.4GHz", FritzboxConnectWLAN(fritz_connect, WLANType.WLAN_2_4_GHZ).stats().influx_data())
    influxp.print("wlan_5GHz", FritzboxConnectWLAN(fritz_connect, WLANType.WLAN_5_GHZ).stats().influx_data())
    influxp.print("wlan_Guest", FritzboxConnectWLAN(fritz_connect, WLANType.WLAN_GUEST).stats().influx_data())
    influxp.print("wan", FritzboxConnectWAN(fritz_connect).stats().influx_data())
    influxp.print("network", FritzboxConnectNetwork(fritz_connect).stats().influx_data())


if __name__ == '__main__':
    execute()
