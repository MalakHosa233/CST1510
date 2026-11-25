"""
db.py - Week 10: how the rest of the project connects to the database.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "DATA" / "app.db"


def connect_database(path=DB_PATH):
    """Open the database file (it is created if it does not exist) and return the connection."""
    path.parent.mkdir(exist_ok=True)
    return sqlite3.connect(path)
