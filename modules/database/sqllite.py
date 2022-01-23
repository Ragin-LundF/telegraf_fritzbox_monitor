import os
import sqlite3 as sql
from sqlite3 import Connection, Cursor
from typing import Iterable


class Database():
    __connection: Connection

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.__connection = sql.connect(f'{dir_path}/fritz.db')
        self.__create_tables()

    def __create_tables(self) -> None:
        with self.__connection:
            self.__connection.execute(self.__create_table_phone_calls())

    def __create_table_phone_calls(self) -> str:
        return """
                CREATE TABLE if not exists PHONE_CALLS (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    call_id varchar(30) NOT NULL,
                    call_name VARCHAR(255),
                    call_number VARCHAR(100),
                    call_duration NUMBER(8, 0),
                    call_type NUMBER(2,0) NOT NULL,
                    call_date NUMBER(12,0) NOT NULL
                );
            """

    def insert(self, sql_query: str, data: Iterable) -> None:
        with self.__connection:
            self.__connection.executemany(sql_query, data)

    def select(self, sql_query) -> list:
        with self.__connection:
            return self.__connection.execute(sql_query).fetchall()

    def execute(self, sql_query) -> None:
        with self.__connection:
            self.__connection.execute(sql_query)
