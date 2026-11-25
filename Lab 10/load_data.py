"""
load_data.py - Week 10: fill the database. Safe to run again.

Run it:  python load_data.py
"""

from pathlib import Path

from app_model.db import connect_database
from app_model.records import count_records, load_csv
from app_model.schema import create_user_table
from app_model.users import migrate_users_file

DATA_FOLDER = Path(__file__).parent / "DATA"


if __name__ == "__main__":
    conn = connect_database()
    create_user_table(conn)

    csv_file = DATA_FOLDER / "raw.csv"
    if csv_file.exists():
        load_csv(conn, csv_file)
        print(f"Loaded {count_records(conn)} rows into the records table.")
    else:
        print("DATA/raw.csv not found - run fetch_data.py first.")

    moved = migrate_users_file(conn, DATA_FOLDER / "users.txt")
    print(f"Moved {moved} user(s) from users.txt into the users table.")
    conn.close()
