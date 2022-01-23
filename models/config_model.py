from dataclasses import dataclass


@dataclass
class ConfigurationModel:
    """Contains Configuration data"""

    def __init__(self):
        self.connection_address: str = ""
        self.connection_username: str = ""
        self.connection_password: str = ""
        self.connection_port: str = ""
        self.defaults_database: str = "FritzBox"
        self.defaults_phone_days: int = 1
        self.defaults_phone_days_kept: int = 5
        self.features_enable_phone_call_tracking: bool = True

    def set_connection_address(self, address: str) -> None:
        self.connection_address = address

    def set_connection_username(self, username: str) -> None:
        self.connection_username = username

    def set_connection_password(self, password: str) -> None:
        self.connection_password = password

    def set_connection_port(self, port: str) -> None:
        self.connection_port = port

    def set_defaults_database(self, database: str) -> None:
        self.defaults_database = database

    def set_defaults_phone_days(self, phone_days: str) -> None:
        self.defaults_phone_days = phone_days

    def set_defaults_phone_days_kept(self, phone_days_kept: str) -> None:
        self.defaults_phone_days_kept = phone_days_kept

    def set_features_enable_phone_call_tracking(self, phone_tracking: bool) -> None:
        self.features_enable_phone_call_tracking = phone_tracking
