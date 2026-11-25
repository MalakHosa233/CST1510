"""
users.py - Week 10: everything about users, now stored in the database.

generate_hash and is_valid_hash are the Week 9 functions, unchanged.
register_user and login_user keep the same shape: they return (True or False, message).
"""

import sqlite3

import bcrypt


# ---- passwords (Week 9) -----------------------------------------------------

def generate_hash(password):
    """Turn a password into a bcrypt hash (returned as text)."""
    byte_password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(byte_password, salt)
    return hashed.decode("utf-8")


def is_valid_hash(password, hashed):
    """True if the password matches the stored hash."""
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))


# ---- SQL: create, read, update, delete -------------------------------------

def add_user(conn, username, password_hash, role="user"):
    """INSERT one user. Raises sqlite3.IntegrityError if the username is taken."""
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
        (username, password_hash, role),
    )
    conn.commit()


def get_user(conn, username):
    """SELECT one user: (id, username, password_hash, role), or None."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cur.fetchone()


def get_all_users(conn):
    """SELECT every user."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    return cur.fetchall()


def update_role(conn, username, new_role):
    """UPDATE one user's role."""
    cur = conn.cursor()
    cur.execute("UPDATE users SET role = ? WHERE username = ?", (new_role, username))
    conn.commit()


def delete_user(conn, username):
    """DELETE one user. (Without the WHERE it would delete everybody!)"""
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()


# ---- register and log in (Week 9, now using the database) --------------------

def register_user(conn, username, password):
    """Add a new user. Returns (True or False, a message)."""
    username = username.strip()
    if username == "":
        return False, "Username cannot be empty."
    if len(password) < 8:
        return False, "Password must be at least 8 characters."
    try:
        add_user(conn, username, generate_hash(password))
    except sqlite3.IntegrityError:          # the UNIQUE rule on username
        return False, "That username is already taken."
    return True, "Registered. You can log in now."


def login_user(conn, username, password):
    """Check a username and password. Returns (True or False, a message)."""
    user = get_user(conn, username.strip())
    if user is not None and is_valid_hash(password, user[2]):
        return True, "Welcome back!"
    return False, "Wrong username or password."      # same message for both problems


def migrate_users_file(conn, path):
    """Copy the users from the Week 9 users.txt into the database. Returns how many were added."""
    if not path.exists():
        return 0
    added = 0
    with open(path, "r") as file:
        for line in file:
            name, password_hash = line.strip().split(",", 1)
            if get_user(conn, name) is None:
                add_user(conn, name, password_hash)
                added += 1
    return added
