from datetime import datetime, timedelta, date, time
from enum import Enum

from fritzconnection.lib.fritzcall import RECEIVED_CALL_TYPE, MISSED_CALL_TYPE, OUT_CALL_TYPE

from models.phone.fritzbox_phone_model import FritzboxPhoneModel
from modules.fritz_connect import FritzboxConnect


class FritzboxConnectPhone:
    def __init__(self, fc: FritzboxConnect):
        self.__FC_CALL = fc.call()
        self.__DB = fc.database()
        self.__DAYS = fc.config().defaults_phone_days
        self.__DAYS_KEPT = fc.config().defaults_phone_days_kept
        self.__CALLS_MISSED = self.__update_db_and_filter(
            self.__FC_CALL.get_missed_calls(days=self.__DAYS),
            CallType.missed)
        self.__CALLS_OUTGOING = self.__update_db_and_filter(
            self.__FC_CALL.get_out_calls(days=self.__DAYS),
            CallType.outgoing)
        self.__CALLS_RECEIVED = self.__update_db_and_filter(
            self.__FC_CALL.get_received_calls(days=self.__DAYS),
            CallType.received)
        self.__cleanup()

    def stats(self) -> FritzboxPhoneModel:
        phone_model = FritzboxPhoneModel(
            count_missed_calls=self.count_missed_calls(),
            count_out_calls=self.count_out_calls(),
            count_received_calls=self.count_received_calls(),
            time_missed_calls=self.time_missed_calls(),
            time_out_calls=self.time_out_calls(),
            time_received_calls=self.time_received_calls()
        )

        return phone_model

    def count_missed_calls(self) -> int:
        return len(self.__CALLS_MISSED)

    def count_out_calls(self) -> int:
        return len(self.__CALLS_OUTGOING)

    def count_received_calls(self) -> int:
        return len(self.__CALLS_RECEIVED)

    def time_missed_calls(self) -> int:
        return self.__aggregate_call_time(self.__CALLS_MISSED)

    def time_out_calls(self) -> int:
        return self.__aggregate_call_time(self.__CALLS_OUTGOING)

    def time_received_calls(self) -> int:
        return self.__aggregate_call_time(self.__CALLS_RECEIVED)

    def __aggregate_call_time(self, phone_calls: list):
        call_time: int = 0
        for entry in phone_calls:
            call_time = call_time + self.__calculate_time_in_seconds(entry.Duration)
        return call_time

    def __calculate_time_in_seconds(self, timestr: str) -> int:
        pt = datetime.strptime(timestr, '%M:%S')
        return pt.second + pt.minute * 60 + pt.hour * 3600

    def __update_db_and_filter(self, phone_calls_fb: list, call_type) -> list:
        self.__check_call_type(call_type)
        sql_query = f"""
            SELECT call_id FROM PHONE_CALLS
             WHERE call_date > {int((self.__datetime_start_today() - timedelta(days=self.__DAYS)).timestamp())}
             AND call_type = {call_type.value}"""
        phone_calls_db = self.__DB.select(sql_query)

        if len(phone_calls_fb) > 0:
            if len(phone_calls_fb) == 0:
                self.__add_calls_to_database(phone_calls_fb)
            else:
                for entry_fb in phone_calls_fb[:]:
                    for entry_db in phone_calls_db:
                        if entry_fb.Id == entry_db[0]:
                            phone_calls_fb.remove(entry_fb)
                self.__add_calls_to_database(phone_calls_fb)
        return phone_calls_fb

    def __add_calls_to_database(self, calls: list) -> None:
        if len(calls) > 0:
            data: list = []
            for entry in calls:
                data.append(
                    (entry.Id, entry.Name, entry.Caller, self.__calculate_time_in_seconds(entry.Duration),
                     self.call_type(entry.Type), int(entry.date.timestamp())))
            self.__DB.insert(
                """
                INSERT INTO PHONE_CALLS (call_id, call_name, call_number, call_duration, call_type, call_date)
                 values
                (?, ?, ?, ?, ?, ?)""",
                data)

    def call_type(self, call_type: str) -> int:
        if int(call_type) == RECEIVED_CALL_TYPE:
            return CallType.received.value
        if int(call_type) == OUT_CALL_TYPE:
            return CallType.outgoing.value
        if int(call_type) == MISSED_CALL_TYPE:
            return CallType.missed.value

    def __check_call_type(self, call_type) -> bool:
        if isinstance(call_type, CallType):
            return True
        raise Exception("Wrong type for enum CallType")

    def __datetime_start_today(self) -> datetime:
        return datetime.combine(date.today(), time())

    def __cleanup(self):
        sql_query = f"""
            DELETE FROM PHONE_CALLS
            WHERE call_date < {int((self.__datetime_start_today() - timedelta(days=self.__DAYS_KEPT)).timestamp())} 
        """
        self.__DB.execute(sql_query)


class CallType(Enum):
    received: int = 0
    outgoing: int = 1
    missed: int = 2
