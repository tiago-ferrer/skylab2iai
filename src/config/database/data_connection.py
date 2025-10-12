from typing import final
import sqlite3

@final
class _SqlDataConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(_SqlDataConnection, cls).__new__(cls)
            cls._instance.db = None
        return cls._instance
    
    def __init__(self):
        if self.db is None:
            self.db = sqlite3.connect('skylab-data.db?mode=ro')

    @final
    def cursor(self):
        return self.db.cursor()