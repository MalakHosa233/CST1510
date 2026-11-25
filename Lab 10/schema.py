"""
schema.py - Week 10: create the tables.
"""


def create_user_table(conn):
    """Create the users table if it is not there yet."""
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            username      TEXT NOT NULL UNIQUE COLLATE NOCASE,
            password_hash TEXT NOT NULL,
            role          TEXT DEFAULT 'user'
        )
    """)
    conn.commit()
