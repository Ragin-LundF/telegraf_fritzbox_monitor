from models.network.fritzbox_network_model import FritzboxNetworkModel
from modules.fritz_connect import FritzboxConnect


class FritzboxConnectNetwork:
    def __init__(self, fc: FritzboxConnect):
        self.__FC_LAN_HOST_CONFIG = fc.read_module('LANHostConfigManagement1', 'GetInfo')
        self.__FC_HOSTS = fc.hosts()
        self.__ALL_HOST_INFO = self.__FC_HOSTS.get_hosts_info()

    def stats(self) -> FritzboxNetworkModel:
        lan_model = FritzboxNetworkModel(
            local_dns=self.local_dns(),
            host_numbers=self.host_numbers(),
            active_hosts=self.active_hosts(),
            active_hosts_lan=self.active_hosts_lan(),
            active_hosts_wlan=self.active_hosts_wlan(),
            hosts_lan=self.hosts_lan(),
            hosts_wlan=self.hosts_wlan()
        )

        return lan_model

    def local_dns(self) -> str:
        return self.__FC_LAN_HOST_CONFIG.get('NewDNSServers')

    def host_numbers(self) -> int:
        return self.__FC_HOSTS.host_numbers

    def host_list(self) -> list:
        return self.__ALL_HOST_INFO

    def active_hosts_list(self) -> list:
        return self.__FC_HOSTS.get_active_hosts()

    def active_hosts(self) -> int:
        active = 0
        for host in self.__ALL_HOST_INFO:
            if host['status']:
                active = active+1
        return active

    def active_hosts_lan(self) -> int:
        active = 0
        for host in self.__ALL_HOST_INFO:
            if host['status'] and host['interface_type'] == 'Ethernet':
                active = active + 1
        return active

    def active_hosts_wlan(self) -> int:
        active = 0
        for host in self.__ALL_HOST_INFO:
            if host['status'] and host['interface_type'] == '802.11':
                active = active + 1
        return active

    def hosts_lan(self) -> int:
        hosts = 0
        for host in self.__ALL_HOST_INFO:
            if host['interface_type'] == 'Ethernet':
                hosts = hosts + 1
        return hosts

    def hosts_wlan(self) -> int:
        hosts = 0
        for host in self.__ALL_HOST_INFO:
            if host['interface_type'] == '802.11':
                hosts = hosts + 1
        return hosts
