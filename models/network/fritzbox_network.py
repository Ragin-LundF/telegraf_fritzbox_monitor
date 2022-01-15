from dataclasses import dataclass

from models.fritzbox_model_interface import FritzboxModelInterface
from modules.influx_print import InfluxPrint


@dataclass
class FritzboxNetwork(FritzboxModelInterface):
    """Contains Network data"""

    def __init__(self, local_dns: str, host_numbers: int, active_hosts: int, active_hosts_lan: int,
                 active_hosts_wlan: int, hosts_lan: int, hosts_wlan: int):
        self.local_dns: str = local_dns
        self.host_numbers: int = host_numbers
        self.active_hosts: int = active_hosts
        self.active_hosts_lan: int = active_hosts_lan
        self.active_hosts_wlan: int = active_hosts_wlan
        self.hosts_lan: int = hosts_lan
        self.hosts_wlan: int = hosts_wlan

    def influx_data(self):
        influx_result = list()
        influx_result = InfluxPrint.append(influx_result, "LocalDNSServer", self.local_dns)
        influx_result = InfluxPrint.append(influx_result, "HostNumberOfEntries", self.host_numbers)
        influx_result = InfluxPrint.append(influx_result, "HostsActive", self.active_hosts)
        influx_result = InfluxPrint.append(influx_result, "HostsActiveLAN", self.active_hosts_lan)
        influx_result = InfluxPrint.append(influx_result, "HostsActiveWLAN", self.active_hosts_wlan)
        influx_result = InfluxPrint.append(influx_result, "HostsKnown", self.host_numbers)
        influx_result = InfluxPrint.append(influx_result, "HostsKnownLAN", self.hosts_lan)
        influx_result = InfluxPrint.append(influx_result, "HostsKnownWLAN", self.hosts_wlan)

        return ",".join(influx_result)
