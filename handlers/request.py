import sqlite3


def connect():
    return sqlite3.connect("bot.db")


def create_tables():

    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        telegram_username TEXT,
        instagram_username TEXT,
        status TEXT,
        reason TEXT,
        email TEXT
    )
    """)

    db.commit()
    db.close()


def save_request(data):

    db = connect()
    cursor = db.cursor()

    cursor.execute("""
    INSERT INTO requests
    (
    user_id,
    telegram_username,
    instagram_username,
    status,
    reason,
    email
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        data["user_id"],
        data["telegram_username"],
        data["instagram_username"],
        data["status"],
        data["reason"],
        data["email"]
    ))

    db.commit()
    db.close()