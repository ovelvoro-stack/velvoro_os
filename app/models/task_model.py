from app.database import get_connection

def fetch_today_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            status TEXT,
            created_at DATE
        )
    """)

    cursor.execute("""
        SELECT id, title, status
        FROM tasks
        WHERE DATE(created_at) = DATE('now')
    """)

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]
