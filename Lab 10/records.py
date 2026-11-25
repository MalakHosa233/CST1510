"""
records.py - Week 10: your API data, stored in the 'records' table.

The table is created from raw.csv, so its columns are whatever your data has.
Each row can be found by its row_id (SQLite's built-in rowid).
"""

import pandas as pd

TABLE = "records"


def load_csv(conn, csv_path):
    """Copy a CSV file into the records table (replacing what was there). Returns the number of rows."""
    df = pd.read_csv(csv_path)
    df.to_sql(TABLE, conn, if_exists="replace", index=False)
    return len(df)


def get_columns(conn):
    """The column names of the records table."""
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {TABLE} LIMIT 0")
    return [column[0] for column in cur.description]


def get_all_records(conn):
    """Every row, as a table, with a row_id column at the front."""
    return pd.read_sql(f"SELECT rowid AS row_id, * FROM {TABLE}", conn)


def count_records(conn):
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {TABLE}")
    return cur.fetchone()[0]


def _check_column(conn, column):
    """A ? can protect a value but not a column NAME, so names are checked against the real list."""
    if column not in get_columns(conn):
        raise ValueError(f"Unknown column: {column}")


def search_records(conn, column, text):
    """Rows where a column contains some text."""
    _check_column(conn, column)
    sql = f"SELECT rowid AS row_id, * FROM {TABLE} WHERE {column} LIKE ?"
    return pd.read_sql(sql, conn, params=(f"%{text}%",))


def add_record(conn, values):
    """INSERT one row. 'values' is a dictionary {column: value}."""
    for column in values:
        _check_column(conn, column)
    names = ", ".join(values)
    marks = ", ".join("?" for _ in values)
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {TABLE} ({names}) VALUES ({marks})", tuple(values.values()))
    conn.commit()


def update_record(conn, row_id, column, value):
    """UPDATE one value in one row. Returns how many rows changed (0 if the row_id does not exist)."""
    _check_column(conn, column)
    cur = conn.cursor()
    cur.execute(f"UPDATE {TABLE} SET {column} = ? WHERE rowid = ?", (value, row_id))
    conn.commit()
    return cur.rowcount


def delete_record(conn, row_id):
    """DELETE one row. Returns how many rows were deleted."""
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {TABLE} WHERE rowid = ?", (row_id,))
    conn.commit()
    return cur.rowcount
