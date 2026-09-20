import os
import sqlite3

APP_NAME = "Faith Glory Church Reminder"

def get_database_path():
    appdata = os.getenv("APPDATA")
    folder = os.path.join(appdata, APP_NAME)
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "church.db")

DB_NAME = get_database_path()

def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS birthdays(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birthday TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weddings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        husband TEXT NOT NULL,
        wife TEXT NOT NULL,
        anniversary TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


# ---------------- Birthdays ----------------

def add_birthday(name, birthday):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO birthdays(name,birthday) VALUES(?,?)",
        (name, birthday)
    )

    conn.commit()
    conn.close()


def get_birthdays():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, birthday
        FROM birthdays
        ORDER BY
            substr(birthday,4,2),
            substr(birthday,1,2)
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_birthday(member_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM birthdays WHERE id=?",
        (member_id,)
    )

    conn.commit()
    conn.close()


def update_birthday(member_id, name, birthday):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE birthdays
        SET name=?, birthday=?
        WHERE id=?
    """, (name, birthday, member_id))

    conn.commit()
    conn.close()


# ---------------- Weddings ----------------

def add_wedding(husband, wife, anniversary):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO weddings(husband,wife,anniversary)
        VALUES(?,?,?)
    """, (husband, wife, anniversary))

    conn.commit()
    conn.close()


def get_weddings():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id,husband,wife,anniversary
        FROM weddings
        ORDER BY husband
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_wedding(member_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM weddings WHERE id=?",
        (member_id,)
    )

    conn.commit()
    conn.close()


def update_wedding(member_id, husband, wife, anniversary):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE weddings
        SET husband=?, wife=?, anniversary=?
        WHERE id=?
    """, (husband, wife, anniversary, member_id))

    conn.commit()
    conn.close()


create_tables()
