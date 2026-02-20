import sqlite3
from werkzeug.security import generate_password_hash

def init_db():
    conn = sqlite3.connect("smartcity.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        description TEXT,
        category TEXT,
        location TEXT,
        urgency TEXT,
        priority_score REAL,
        status TEXT,
        created_at TEXT
    )
    """)

    # Create default admin if not exists
    cursor.execute("SELECT * FROM users WHERE email='admin@smartcity.com'")
    if not cursor.fetchone():
        cursor.execute("""
        INSERT INTO users (name, email, password, role)
        VALUES (?, ?, ?, ?)
        """, (
            "Admin",
            "admin@smartcity.com",
            generate_password_hash("admin123"),
            "admin"
        ))

    conn.commit()
    conn.close()