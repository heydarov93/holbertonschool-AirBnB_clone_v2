#!/usr/bin/python3
"""Contains storage for database (not file storage)"""

from sqlalchemy import create_engine
from os import environ

HBNB_ENV
HBNB_MYSQL_USER
HBNB_MYSQL_PWD
HBNB_MYSQL_HOST
HBNB_MYSQL_DB
HBNB_TYPE_STORAGE


class DBStorage:
    """DataBase Storage Engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the engine"""
        self.__engine = create_engine(f"mysql+mysqldb)://\
                {}:{}@{}/{}"
